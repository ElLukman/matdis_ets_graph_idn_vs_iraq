# =================================================================
# APLIKASI SISTEM PAKAR ANALISIS TIMNAS
# File: main.py
# Deskripsi: Memenuhi Rubrik EAS B.3 (8 Tombol) & B.4 (Custom Input)
# Fitur Baru: Trace Logic untuk Inferensi 5 & Cheat Sheet Query
# =================================================================

import streamlit as st
from pyswip import Prolog
import pandas as pd
import time

# --- KONFIGURASI FILE KB ---
KB_FILE = 'prolog_kb.pl'
st.set_page_config(page_title="Sistem Pakar Timnas (EAS)", layout="wide", page_icon="⚽")

# --- INISIALISASI PROLOG ---
if 'prolog' not in st.session_state:
    try:
        prolog = Prolog()
        prolog.consult(KB_FILE)
        st.session_state.prolog = prolog
        st.session_state.kb_status = "✅ KB Terhubung"
    except Exception as e:
        st.session_state.kb_status = f"❌ Error: {e}"
        st.error(f"Gagal memuat {KB_FILE}. Pastikan file berada di satu folder.")

# --- HELPER FUNCTIONS ---
def clean_text(value):
    """Merapikan output string dari Prolog."""
    if isinstance(value, str):
        return value.replace('_', ' ').title()
    return value

def run_query(query_str):
    """Wrapper query standar untuk tombol biasa."""
    prolog = st.session_state.prolog
    try:
        results = list(prolog.query(query_str))
        if not results: return None
        
        clean_data = []
        for row in results:
            clean_row = {k: clean_text(v) for k, v in row.items()}
            clean_data.append(clean_row)
        return clean_data
    except Exception as e:
        st.error(f"Syntax Error: {e}")
        return None

def check_step(query_str):
    """Cek kebenaran boolean untuk visualisasi proses (Inferensi 5)."""
    prolog = st.session_state.prolog
    try:
        res = list(prolog.query(query_str))
        return len(res) > 0
    except:
        return False

# --- UI UTAMA ---
def main():
    st.title("⚽ Sistem Inferensi: Analisis Timnas Indonesia")
    st.markdown(f"**Status KB:** {st.session_state.kb_status}")
    st.divider()

    # BAGIAN B.3: 8 TOMBOL UJI INFERENSI
    st.header("🔍 Uji Inferensi (8 Skenario Wajib)")
    
    col1, col2 = st.columns(2)

    # --- KOLOM KIRI ---
    with col1:
        # 1. Fakta Squad
        with st.container(border=True):
            st.subheader("1. Cek Squad Starter")
            st.caption("Fakta: `pemain_data(Nama, ..., starter)`")
            if st.button("Jalankan #1"):
                res = run_query("pemain_data(Nama, No, Posisi, _, starter)")
                if res: st.dataframe(res, use_container_width=True)
                else: st.warning("Data tidak ditemukan.")

        # 3. Rule Hub
        with st.container(border=True):
            st.subheader("3. Hub Permainan (Rule)")
            st.caption("Rule: Passing > 350 & Akurasi > 90%")
            if st.button("Jalankan #3"):
                res = run_query("hub_permainan(Pemain)")
                if res: 
                    st.success(f"✅ Hub Ditemukan: **{res[0]['Pemain']}**")
                else: st.warning("Tidak ada data.")

        # 5. RANTAI SEBAB-AKIBAT (VISUALISASI PROSES)
        with st.container(border=True):
            st.subheader("5. Rantai Kekalahan (Trace)")
            st.caption("Menampilkan PROSES logika dari penyebab -> akibat.")
            
            if st.button("Jalankan #5 (Lihat Proses)"):
                st.write("---")
                st.markdown("**🕵️ Memulai Penelusuran Rantai Logika:**")
                
                # STEP 1
                with st.spinner("Cek Kondisi Fisik..."):
                    time.sleep(0.5)
                    if check_step("kelelahan_parah"):
                        st.success("✅ **Langkah 1:** Kelelahan Parah Terdeteksi (Faktor Lingkungan)")
                    else:
                        st.error("❌ Terhenti di Langkah 1.")
                        st.stop()

                # STEP 2
                with st.spinner("Analisis Dampak Performa..."):
                    time.sleep(0.5)
                    if check_step("performa_menurun"):
                        st.success("✅ **Langkah 2:** Performa Fisik Menurun Signifikan")
                    else:
                        st.error("❌ Terhenti di Langkah 2.")
                        st.stop()

                # STEP 3
                with st.spinner("Evaluasi Efektivitas..."):
                    time.sleep(0.5)
                    if check_step("efektivitas_rendah"):
                        st.success("✅ **Langkah 3:** Efektivitas Rendah (Akibat Performa & Strategi)")
                    else:
                        st.error("❌ Terhenti di Langkah 3.")
                        st.stop()

                # STEP 4 (FINAL)
                with st.spinner("Menarik Kesimpulan Akhir..."):
                    time.sleep(0.5)
                    if check_step("analisis_kekalahan_lengkap"):
                        st.success("✅ **KESIMPULAN:** Kekalahan Tak Terelakkan (Valid)")
                        st.balloons()
                    else:
                        st.error("❌ Kesimpulan akhir gagal dibuktikan.")

        # 7. Diagnosa Expert
        with st.container(border=True):
            st.subheader("7. Diagnosa & Solusi")
            st.caption("Solusi konkret untuk masalah 'Lemah Finishing'.")
            if st.button("Jalankan #7"):
                # Menampilkan Diagnosa Lengkap
                res = run_query("diagnosa_lengkap(lemah_finishing, Severity, Kategori, Solusi)")
                if res:
                    st.info(f"**Masalah:** Lemah Finishing")
                    st.write(f"**Severity:** {res[0]['Severity']}")
                    st.write(f"**Solusi:** {res[0]['Solusi']}")
                else:
                    st.warning("Tidak ada solusi ditemukan.")

    # --- KOLOM KANAN ---
    with col2:
        # 2. Statistik Spesifik
        with st.container(border=True):
            st.subheader("2. Statistik Jay Idzes")
            st.caption("Fakta: `statistik_pemain(jay_idzes, ...)`")
            if st.button("Jalankan #2"):
                res = run_query("statistik_pemain(jay_idzes, Kategori, Jumlah, Unit)")
                if res: st.dataframe(res, use_container_width=True)

        # 4. Pemain Vital
        with st.container(border=True):
            st.subheader("4. Pemain Vital (Chain)")
            st.caption("Logika: Hub + Pilar Pertahanan.")
            if st.button("Jalankan #4"):
                res = run_query("pemain_vital(Pemain)")
                if res: st.success(f"✅ Pemain Vital: **{res[0]['Pemain']}**")
                else: st.warning("Tidak ada hasil.")

        # 6. Masalah Kritis
        with st.container(border=True):
            st.subheader("6. Masalah Severity Critical")
            st.caption("Identifikasi masalah dengan skor > 7.")
            if st.button("Jalankan #6"):
                res = run_query("severity_critical(Masalah)")
                if res: st.dataframe(res, use_container_width=True)

        # 8. Statistik Tim (FIXED)
        with st.container(border=True):
            st.subheader("8. Perbandingan Statistik Tim")
            st.caption("Menarik data statistik agregat Timnas.")
            if st.button("Jalankan #8"):
                res = run_query("statistik_tim(indonesia, Kategori, Nilai)")
                if res: st.dataframe(res, use_container_width=True)
                else: st.error("Data statistik tim tidak ditemukan (Cek KB).")

    st.divider()

    # =========================================================
    # BAGIAN B.4: TERMINAL QUERY MANUAL & CONTOH
    # =========================================================
    st.header("⌨️ Terminal Query Manual (Rubrik B.4)")
    
    # CHEAT SHEET QUERY (Permintaan User: Masukkan seluruh contoh query)
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