# =================================================================
# APLIKASI SISTEM PAKAR ANALISIS TIMNAS (SESUAI RUBRIK EAS)
# Kompatibel dengan: prolog_kb_dayanlagi.pl
# =================================================================

import streamlit as st
from pyswip import Prolog
import pandas as pd

# --- KONFIGURASI FILE KB ---
KB_FILE = 'prolog_kb_dayanlagi.pl'

# --- 1. SETUP DAN INISIALISASI PROLOG ---
if 'prolog' not in st.session_state:
    try:
        prolog = Prolog()
        # Menggunakan consult untuk memuat file KB
        prolog.consult(KB_FILE) 
        st.session_state.prolog = prolog
        st.session_state.kb_loaded = True
    except Exception as e:
        st.error(f"❌ Gagal memuat SWI-Prolog atau file '{KB_FILE}'.")
        st.error(f"Detail Error: {e}")
        st.stop()

prolog = st.session_state.prolog

# --- 2. DEFINISI 8 QUERY WAJIB (SESUAI KB BARU) ---
# Daftar ini mencakup Fakta Kompleks, Rule Statistik, dan Rantai Penalaran

inferensi_list = [
    # 1. Fakta Kompleks (Data Pemain)
    {
        "judul": "1. Cek Squad Starter",
        "query": "pemain_data(Nama, No, Posisi, _, starter)",
        "desc": "Mengambil data pemain yang menjadi starter (Predikat 5 argumen)."
    },
    # 2. Rule Statistik Spesifik
    {
        "judul": "2. Statistik Jay Idzes",
        "query": "statistik_pemain(jay_idzes, Kategori, Jumlah, Unit)",
        "desc": "Melihat detail statistik Jay Idzes (Passing, Tackle, Shot, dll)."
    },
    # 3. Rule Logika: Hub Permainan
    {
        "judul": "3. Hub Permainan (Rule B.4)",
        "query": "hub_permainan(Pemain)",
        "desc": "Mencari pemain dengan Passing > 350 DAN Akurasi > 90%."
    },
    # 4. Rule Rantai 3 Langkah: Pemain Vital
    {
        "judul": "4. Pemain Vital (Rule C.3)",
        "query": "pemain_vital(Pemain)",
        "desc": "Rantai Logika: Hub Permainan + Pilar Pertahanan + Penyerang Aktif (All-in-One)."
    },
    # 5. Rule Rantai 4 Langkah: Analisis Kekalahan
    {
        "judul": "5. Rantai Sebab-Akibat Kekalahan",
        "query": "analisis_kekalahan_lengkap",
        "desc": "Membuktikan rantai: Kelelahan -> Performa Turun -> Efektivitas Rendah -> Kekalahan."
    },
    # 6. Identifikasi Masalah Kritis
    {
        "judul": "6. Masalah Severity Critical",
        "query": "severity_critical(Masalah)",
        "desc": "Identifikasi masalah dengan skor kekritisan > 7."
    },
    # 7. Diagnosa Solusi (Expert System)
    {
        "judul": "7. Diagnosa Lemah Finishing",
        "query": "diagnosa_lengkap(lemah_finishing, Severity, Kategori, Solusi)",
        "desc": "Memberikan diagnosa lengkap & solusi untuk masalah finishing."
    },
    # 8. Statistik Tim
    {
        "judul": "8. Perbandingan Statistik Tim",
        "query": "statistik_tim(indonesia, Kategori, Nilai)",
        "desc": "Menarik data statistik agregat Timnas Indonesia."
    }
]

def run_query(query):
    """Fungsi helper untuk menangani output PySwip dengan rapi."""
    try:
        # Menjalankan query
        results = list(prolog.query(query))
        
        # Kasus 1: Query Mengembalikan False (Tidak ada hasil)
        if not results:
            return "❌ False / Tidak Terbukti / Data Tidak Ditemukan."
        
        # Kasus 2: Query Boolean (Hanya True/False tanpa variabel)
        if len(results) == 0: 
             return "✅ True (Proposisi Valid)."
        
        # Kasus 3: Query dengan Variabel (X = ...)
        # Format output menjadi list yang bersih
        output_list = []
        for res in results:
            # Membersihkan nama atom (misal: 'jay_idzes' jadi 'Jay Idzes' jika perlu, atau biarkan raw)
            clean_item = {k: (v.replace('_', ' ').title() if isinstance(v, str) else v) for k, v in res.items()}
            output_list.append(clean_item)
            
        return output_list

    except Exception as e:
        return f"⚠️ Error Syntax Prolog: {e}"

# --- 3. GUI STREAMLIT ---
st.set_page_config(page_title="Sistem Pakar Timnas", layout="wide")

st.title("⚽ Sistem Pakar: Analisis Timnas Indonesia")
st.markdown(f"**Knowledge Base:** `{KB_FILE}` (Versi Lengkap)")
st.markdown("""
Aplikasi ini menggunakan **Prolog** untuk menganalisis data pertandingan Indonesia vs Iraq 
berdasarkan fakta statistik, aturan logika (rules), dan rantai penalaran (causal chain).
""")
st.markdown("---")

# Layout Kolom
col_kb, col_main = st.columns([1, 2])

with col_kb:
    st.info("📂 **Knowledge Base Preview**")
    st.write("Memuat fakta & rules dari file .pl")
    
    with st.expander("📜 Lihat Kode Prolog Asli"):
        try:
            with open(KB_FILE, "r") as f:
                st.code(f.read(), language="prolog")
        except:
            st.error("File tidak ditemukan.")
            
    st.markdown("### 💡 Fitur Logika")
    st.markdown("""
    - **Facts:** Data Pemain, Statistik, Event.
    - **Rules:** Klasifikasi Severity, Peran Pemain.
    - **Chaining:** Analisis Sebab-Akibat Kekalahan.
    """)

with col_main:
    st.header("🔍 Uji Inferensi (8 Skenario)")
    st.write("Klik tombol di bawah untuk menjalankan mesin inferensi:")
    
    # Grid layout untuk tombol (2 kolom x 4 baris)
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    row4 = st.columns(2)
    
    grid_cols = row1 + row2 + row3 + row4
    
    for i, item in enumerate(inferensi_list):
        with grid_cols[i]:
            with st.container(border=True):
                st.subheader(item["judul"])
                st.caption(item["desc"])
                st.code(f"?- {item['query']}", language="prolog")
                
                if st.button(f"Jalankan #{i+1}", key=f"btn_{i}"):
                    hasil = run_query(item["query"])
                    
                    if isinstance(hasil, list):
                        st.success(f"✅ Ditemukan {len(hasil)} Fakta:")
                        # Jika hasil berupa list dictionary, tampilkan sebagai DataFrame atau JSON rapi
                        st.dataframe(pd.DataFrame(hasil), use_container_width=True)
                    elif "True" in str(hasil):
                        st.success(hasil)
                    else:
                        st.warning(hasil)

    # Bagian Query Kustom
    st.markdown("---")
    st.subheader("🔧 Terminal Query Manual")
    st.markdown("Masukkan query Prolog bebas. Contoh: `pencetak_gol(Siapa, iraq, Waktu)` atau `kapten(indonesia, X)`")
    
    user_query = st.text_input("Input Query:", placeholder="Maukkan query disini...")
    
    if st.button("Eksekusi Query Manual"):
        if user_query:
            st.markdown("**Hasil Eksekusi:**")
            res_manual = run_query(user_query)
            if isinstance(res_manual, list):
                st.dataframe(res_manual)
            else:
                st.write(res_manual)
        else:
            st.error("Harap masukkan query.")

# Footer
st.markdown("---")
st.markdown("**Catatan Analisis:**")
st.caption("""
* **Pemain Vital:** Logika KB baru mendefinisikan pemain vital sebagai seseorang yang menjadi Hub Permainan (Passing Tinggi), 
    Pilar Pertahanan (Tackle Tinggi), DAN Penyerang Aktif (Ada Shot). Jay Idzes adalah kandidat kuat untuk logika ini.
* **Analisis Kekalahan:** Menggunakan Rantai 4 Langkah dari faktor Fisik -> Performa -> Strategi -> Hasil Akhir.
""")