# =================================================================
# APLIKASI SISTEM PAKAR ANALISIS TIMNAS
# File: main.py
# =================================================================
# Aplikasi GUI berbasis Streamlit untuk:
# - Menjalankan inferensi logika (First Order Logic) terkait performa Timnas
# - Mengintegrasikan Python dengan SWI-Prolog
# - Menguji rule-based reasoning pada analisis sebab-akibat kekalahan
#
# Teknologi:
# - Python (GUI & kontrol alur)
# - Streamlit (User Interface Interaktif)
# - SWI-Prolog + pyswip (Knowledge Base & Inference Engine)
#
# Tujuan akademik:
# - Demonstrasi reasoning berbasis aturan (rule-based system)
# - Menunjukkan chaining inferensi logika (Penyebab -> Akibat)
# - Visualisasi hasil query Prolog dalam bentuk tabel dan trace logika
# =================================================================

# ============================================================
# IMPORT LIBRARY
# ============================================================
# streamlit
# Framework GUI berbasis web untuk Python
# Digunakan untuk: Layout halaman, Tombol, Tabel, dan Status visualisasi
import streamlit as st

# pyswip.Prolog
# Library Python untuk berinteraksi dengan SWI-Prolog
# Digunakan untuk: Load knowledge base (.pl) dan Menjalankan query Prolog
from pyswip import Prolog

# time
# Digunakan untuk memberikan jeda (delay) pada visualisasi proses inferensi (Trace)
import time

# ============================================================
# 1. SETUP APLIKASI & LOAD KNOWLEDGE BASE
# ============================================================
# Nama file Knowledge Base Prolog
# Berisi fakta statistik pemain, data pertandingan, dan aturan fishbone
KB_FILE = 'prolog_kb_dayanlagi.pl'

# Konfigurasi halaman Streamlit
# layout="wide" agar tampilan lebih lebar dan nyaman untuk tabel data
st.set_page_config(page_title="Sistem Pakar Timnas (EAS)", layout="wide", page_icon="⚽")

# ============================================================
# Inisialisasi Engine Prolog
# ============================================================
# Menggunakan st.session_state agar:
# - Prolog hanya di-load sekali saat aplikasi mulai
# - Tidak reload setiap kali user menekan tombol (efisiensi)
if 'prolog' not in st.session_state:
    try:
        # Membuat instance Prolog
        prolog = Prolog()
        # Load knowledge base (.pl)
        prolog.consult(KB_FILE)
        # Simpan ke session_state
        st.session_state.prolog = prolog
        st.session_state.kb_status = "✅ KB Terhubung"
    except Exception as e:
        # Jika gagal load KB: tampilkan error
        st.session_state.kb_status = f"❌ Error: {e}"
        st.error(f"Gagal memuat {KB_FILE}. Pastikan file berada di satu folder.")

# ============================================================
# 2. HELPER FUNCTIONS (Fungsi Bantu)
# ============================================================
def clean_text(value):
    """
    Membersihkan output string dari Prolog.
    Contoh: mengubah 'jay_idzes' menjadi 'Jay Idzes' agar lebih enak dibaca.
    """
    if isinstance(value, str):
        return value.replace('_', ' ').title()
    return value

def run_query(query_str):
    """
    Wrapper standar untuk menjalankan query Prolog.
    Mengembalikan:
    - None jika gagal/kosong
    - List of Dictionaries jika berhasil (siap jadi DataFrame)
    """
    prolog = st.session_state.prolog
    try:
        results = list(prolog.query(query_str))
        if not results: return None
        
        # Format hasil ke list of dicts yang bersih
        clean_data = []
        for row in results:
            clean_row = {k: clean_text(v) for k, v in row.items()}
            clean_data.append(clean_row)
        return clean_data
    except Exception as e:
        st.error(f"Syntax Error: {e}")
        return None

def check_step(query_str):
    """
    Khusus untuk mengecek kebenaran boolean (True/False).
    Digunakan untuk visualisasi langkah-demi-langkah pada Inferensi Rantai (#5).
    """
    prolog = st.session_state.prolog
    try:
        res = list(prolog.query(query_str))
        return len(res) > 0
    except:
        return False

# ============================================================
# 3. UI UTAMA (Interface Pengguna)
# ============================================================
def main():
    st.title("⚽ Sistem Inferensi: Analisis Timnas Indonesia")
    st.markdown(f"**Status KB:** {st.session_state.kb_status}")
    st.divider()

    # =========================================================
    # BAGIAN B.3: 8 TOMBOL UJI INFERENSI
    # =========================================================
    # Menampilkan 8 skenario pengujian logika sesuai rubrik penilaian.
    # Terbagi dalam 2 kolom untuk kerapian layout.
    st.header("🔍 Uji Inferensi (8 Skenario Wajib)")
    
    col1, col2 = st.columns(2)

    # --- KOLOM KIRI ---
    with col1:
        # Inferensi 1: Fakta Kompleks
        # Menguji pengambilan data pemain starter dari predikat N-ary
        with st.container(border=True):
            st.subheader("1. Cek Squad Starter")
            st.caption("Fakta: `pemain_data(Nama, ..., starter)`")
            if st.button("Jalankan #1"):
                res = run_query("pemain_data(Nama, No, Posisi, _, starter)")
                if res: st.dataframe(res, use_container_width=True)
                else: st.warning("Data tidak ditemukan.")

        # Inferensi 3: Rule Logika (Hub)
        # Menguji Rule B.4: Pemain dengan Passing > 350 dan Akurasi > 90%
        with st.container(border=True):
            st.subheader("3. Hub Permainan (Rule B.4)")
            st.caption("Mencari pemain: Passing > 350 & Akurasi > 90%")
            if st.button("Jalankan #3"):
                res = run_query("hub_permainan(Pemain)")
                if res: 
                    st.success(f"✅ Hub Ditemukan: **{res[0]['Pemain']}**")
                else: st.warning("Tidak ada pemain yang memenuhi kriteria Hub.")

        # Inferensi 5: Rantai Sebab-Akibat (SHOW PROCESS)
        # Mendemonstrasikan 'Chain of Reasoning' dari kondisi fisik ke kekalahan
        with st.container(border=True):
            st.subheader("5. Rantai Sebab-Akibat Kekalahan")
            st.caption("Menelusuri alur logika dari Kelelahan -> Kekalahan.")
            
            if st.button("Jalankan #5 (Lihat Proses)"):
                # Container st.status untuk animasi proses berpikir sistem
                with st.status("🕵️ Sedang menganalisis rantai kausalitas...", expanded=True) as status:
                    time.sleep(0.5) # Efek loading agar terlihat prosesnya
                    
                    # LANGKAH 1: Cek Premis Awal (Lingkungan -> Fisik)
                    st.write("**Langkah 1: Cek Kelelahan Fisik**")
                    if check_step("kelelahan_parah"):
                        st.success("✅ Valid: Kelelahan Parah (Lingkungan + Jadwal Padat)")
                    else:
                        st.error("❌ Terputus: Kelelahan tidak terbukti.")
                        st.stop()
                    
                    # LANGKAH 2: Dampak Fisik ke Performa
                    time.sleep(0.3)
                    st.write("**Langkah 2: Dampak ke Performa**")
                    if check_step("performa_menurun"):
                        st.success("✅ Valid: Performa Fisik Menurun")
                    else:
                        st.error("❌ Terputus di performa.")
                        st.stop()

                    # LANGKAH 3: Kombinasi Performa & Taktik
                    time.sleep(0.3)
                    st.write("**Langkah 3: Efektivitas Permainan**")
                    if check_step("efektivitas_rendah"):
                        st.success("✅ Valid: Efektivitas Rendah (Performa Turun + Strategi Lemah)")
                    else:
                        st.error("❌ Terputus di efektivitas.")
                        st.stop()

                    # LANGKAH 4 (FINAL): Konklusi Kekalahan
                    time.sleep(0.3)
                    st.write("**Langkah 4: Kesimpulan Akhir**")
                    if check_step("analisis_kekalahan_lengkap"):
                        st.success("✅ **TERBUKTI:** Kekalahan Tak Terelakkan (Efektivitas Rendah + Masalah Kritis)")
                        status.update(label="Analisis Selesai: Rantai Logika Valid!", state="complete", expanded=False)
                    else:
                        st.error("❌ Kesimpulan akhir gagal dibuktikan.")
                        status.update(label="Analisis Gagal", state="error")

        # Inferensi 7: Diagnosa Expert System
        # Memberikan rekomendasi solusi berdasarkan masalah spesifik
        with st.container(border=True):
            st.subheader("7. Diagnosa Lemah Finishing")
            st.caption("Memberikan solusi untuk masalah 'lemah_finishing'.")
            if st.button("Jalankan #7"):
                # Query ini sekarang pasti jalan karena KB sudah diperbaiki
                q = "diagnosa_lengkap(lemah_finishing, Severity, Kategori, Solusi)"
                res = run_query(q)
                if res:
                    st.info(f"**Masalah:** Lemah Finishing")
                    st.write(f"**Severity:** {res[0]['Severity']}")
                    st.write(f"**Solusi:** {res[0]['Solusi']}")
                else:
                    st.warning("Diagnosa gagal (Cek rule rekomendasi di KB).")

    # --- KOLOM KANAN ---
    with col2:
        # Inferensi 2: Statistik Spesifik
        # Mengambil fakta statistik detail untuk satu pemain (Jay Idzes)
        with st.container(border=True):
            st.subheader("2. Statistik Jay Idzes")
            st.caption("Fakta: `statistik_pemain(jay_idzes, ...)`")
            if st.button("Jalankan #2"):
                res = run_query("statistik_pemain(jay_idzes, Kategori, Jumlah, Unit)")
                if res: st.dataframe(res, use_container_width=True)

        # Inferensi 4: Pemain Vital (Chain)
        # Rantai 3 langkah: Hub + Pilar Pertahanan + Penyerang Aktif
        with st.container(border=True):
            st.subheader("4. Pemain Vital (Chain)")
            st.caption("Logika: Hub + Pilar Pertahanan + Penyerang Aktif")
            if st.button("Jalankan #4"):
                res = run_query("pemain_vital(Pemain)")
                if res: st.success(f"✅ Pemain Vital: **{res[0]['Pemain']}**")
                else: st.warning("Tidak ada pemain vital.")

        # Inferensi 6: Masalah Kritis
        # Mengidentifikasi masalah dengan skor urgensi > 7
        with st.container(border=True):
            st.subheader("6. Masalah Severity Critical")
            st.caption("Identifikasi masalah dengan skor > 7.")
            if st.button("Jalankan #6"):
                res = run_query("severity_critical(Masalah)")
                if res: st.dataframe(res)

        # Inferensi 8: Statistik Tim
        # Menarik data agregat untuk seluruh tim
        with st.container(border=True):
            st.subheader("8. Perbandingan Statistik Tim")
            st.caption("Menarik data statistik agregat Timnas.")
            if st.button("Jalankan #8"):
                # Error 'existence_error' diperbaiki dengan merapikan KB
                res = run_query("statistik_tim(indonesia, Kategori, Nilai)")
                if res: st.dataframe(res, use_container_width=True)
                else: st.error("Data statistik tim tidak ditemukan.")

    st.divider()

    # =========================================================
    # BAGIAN B.4: TERMINAL QUERY MANUAL & CONTOH
    # =========================================================
    st.header("⌨️ Terminal Query Manual (Rubrik B.4)")
    
    # Cheat Sheet untuk memudahkan pengujian manual
    with st.expander("📝 Klik di sini untuk melihat DAFTAR CONTOH QUERY (Copy-Paste)"):
        st.markdown("""
        Salin query di bawah ini ke dalam kotak input:
        1.  `pemain_kunci(X)`
        2.  `hub_permainan(X)`
        3.  `pemain_vital(X)`
        4.  `masalah_penyerangan_kritis`
        5.  `analisis_kekalahan_lengkap`
        6.  `statistik_pemain(jay_idzes, passing, X, total_operan)`
        7.  `operan_sukses(jay_idzes, X, Y)`
        8.  `butuh_revisi_total_strategi`
        9.  `pemain_naturalisasi(X)`
        10. `kapten(indonesia, Siapa)`
        """)

    st.info("Masukkan query Prolog valid (tanpa titik di akhir).")
    
    col_input, col_act = st.columns([3, 1])
    with col_input:
        user_input = st.text_input("Input Query:", placeholder="Contoh: kapten(indonesia, X)", key="custom_q")
    with col_act:
        st.write("") 
        st.write("")
        btn_exec = st.button("Eksekusi Manual", type="primary", use_container_width=True)
    
    if btn_exec:
        if user_input:
            res = run_query(user_input)
            if res is not None:
                if len(res) > 0:
                    st.success(f"✅ Ditemukan {len(res)} Fakta")
                    st.dataframe(res, use_container_width=True)
                else: 
                    st.success("✅ TRUE (Valid)")
            else:
                st.warning("❌ FALSE (Tidak Terbukti / Data Kosong)")
        else:
            st.error("Input tidak boleh kosong.")

if __name__ == "__main__":
    main()