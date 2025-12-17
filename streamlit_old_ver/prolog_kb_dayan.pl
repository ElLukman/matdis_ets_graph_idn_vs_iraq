% =================================================================
% FILE: prolog_kb.pl
% Knowledge Base - Analisis Kekalahan Timnas Indonesia vs Iraq
% Putaran 4 Kualifikasi Piala Dunia 2026
% Pertandingan: Iraq 1-0 Indonesia (12 Oktober 2025, King Abdullah Sports City, Jeddah)
% =================================================================

% --- TEMA: Analisis Kekalahan Timnas Indonesia Melawan Iraq ---
% Menggunakan pendekatan Fishbone Diagram & FOL untuk identifikasi
% akar penyebab kekalahan dan rekomendasi perbaikan

% =================================================================
% BAGIAN A: FACTS (Proposisi Dasar) - Minimal 15 Facts
% =================================================================

% --- A.1 FACTS: Data Pertandingan ---
pertandingan(indonesia_vs_iraq, '2025-10-12', jeddah_saudi_arabia).
skor_akhir(indonesia, 0).
skor_akhir(iraq, 1).
lokasi_pertandingan(king_abdullah_sports_city).
venue_netral(jeddah_saudi_arabia).
pencetak_gol(iraq, zidane_iqbal, 76).

% --- A.2 FACTS: Kondisi Tim Indonesia ---
pelatih(indonesia, patrick_kluivert).
ranking_fifa(indonesia, 118).
pemain_kunci_absen(maarten_paes). % Kiper utama absen karena akumulasi kartu
formasi_yang_digunakan(indonesia, '4-3-3').
jumlah_shot(indonesia, 5).
shot_on_target(indonesia, 0). % Tidak ada tembakan tepat sasaran
penguasaan_bola(indonesia, 48). % Persentase penguasaan bola

% --- A.3 FACTS: Kondisi Tim Iraq ---
pelatih(iraq, graham_arnold).
ranking_fifa(iraq, 58).
formasi_yang_digunakan(iraq, '4-2-3-1').
pemain_bintang(iraq, aymen_hussein).
pemain_bintang(iraq, ali_jasim).
pemain_bintang(iraq, zidane_iqbal).
penguasaan_bola(iraq, 52).
jumlah_shot(iraq, 8).
shot_on_target(iraq, 3).

% --- A.4 FACTS: Akar Penyebab Kekalahan (Kategori Fishbone) ---
% Kategori: Man (Manusia/Pemain)
akar_penyebab(kurangnya_pengalaman_pemain, man).
akar_penyebab(kurangnya_konsentrasi_pemain, man).
akar_penyebab(pemain_kunci_absen, man).
akar_penyebab(perbedaan_kualitas_pemain, man).
akar_penyebab(lemah_finishing, man).

% Kategori: Method (Metode/Strategi)
akar_penyebab(kurangnya_taktik_penyerangan, method).
akar_penyebab(kebingungan_opsi_operan, method).
akar_penyebag(substitusi_kurang_efektif, method).
akar_penyebab(pressing_tidak_efektif, method).
akar_penyebab(gagal_breakdown_defense_iraq, method).

% Kategori: Environment (Lingkungan)
akar_penyebab(kondisi_cuaca_panas_arab_saudi, environment).
akar_penyebab(kondisi_lapangan_cepat, environment).
akar_penyebab(venue_netral_menguntungkan_iraq, environment).
akar_penyebab(jadwal_padat_3_hari, environment).

% Kategori: Material (Fasilitas/Sumber Daya)
akar_penyebab(kurangnya_fasilitas_pemulihan, material).
akar_penyebab(keterbatasan_kedalaman_skuad, material).

% --- A.5 FACTS: Faktor Kekuatan Lawan (Iraq) ---
kekuatan_lawan(iraq, high_pressing_intensity).
kekuatan_lawan(iraq, physical_dominance).
kekuatan_lawan(iraq, experienced_core_players).
kekuatan_lawan(iraq, tactical_discipline).
kekuatan_lawan(iraq, midfield_control).

% --- A.6 FACTS: Statistik Pertandingan ---
statistik_pertandingan(corners, indonesia, 3).
statistik_pertandingan(corners, iraq, 5).
statistik_pertandingan(fouls, indonesia, 12).
statistik_pertandingan(fouls, iraq, 14).
statistik_pertandingan(yellow_cards, indonesia, 2).
statistik_pertandingan(yellow_cards, iraq, 2).
statistik_pertandingan(red_cards, iraq, 1). % Zaid Tahseen kartu merah menit 90+

% --- A.7 FACTS: Klasifikasi Severity/Kekritisan Masalah ---
tingkat_kekritisan(lemah_finishing, 9). % Sangat kritis
tingkat_kekritisan(pressing_tidak_efektif, 8). % Kritis
tingkat_kekritisan(kurangnya_pengalaman_pemain, 7). % Moderate-High
tingkat_kekritisan(pemain_kunci_absen, 7).
tingkat_kekritisan(kondisi_cuaca_panas_arab_saudi, 6). % Moderate
tingkat_kekritisan(kebingungan_opsi_operan, 8).
tingkat_kekritisan(gagal_breakdown_defense_iraq, 9).

% =================================================================
% BAGIAN B: RULES (Implikasi/Inferensi) - Minimal 8 Rules
% =================================================================

% --- B.1 RULES: Klasifikasi Tingkat Kritis ---
% Adaptasi dari template severity classification
severity_minor(Masalah) :- 
    tingkat_kekritisan(Masalah, Score), 
    Score < 4.

severity_moderate(Masalah) :- 
    tingkat_kekritisan(Masalah, Score), 
    Score >= 4, 
    Score =< 7.

severity_critical(Masalah) :- 
    tingkat_kekritisan(Masalah, Score), 
    Score > 7.

% --- B.2 RULES: Identifikasi Kategori Masalah ---
masalah_teknis(Masalah) :- 
    akar_penyebab(Masalah, man).

masalah_strategis(Masalah) :- 
    akar_penyebab(Masalah, method).

masalah_eksternal(Masalah) :- 
    akar_penyebab(Masalah, environment).

masalah_infrastruktur(Masalah) :- 
    akar_penyebab(Masalah, material).

% --- B.3 RULES: Analisis Kelemahan Utama ---
% Rule: Jika lemah finishing DAN shot on target = 0, maka masalah penyerangan kritis
masalah_penyerangan_kritis :- 
    severity_critical(lemah_finishing),
    shot_on_target(indonesia, 0).

% Rule: Jika pressing tidak efektif DAN Iraq kontrol midfield, maka masalah kontrol_permainan
masalah_kontrol_permainan :- 
    severity_critical(pressing_tidak_efektif),
    kekuatan_lawan(iraq, midfield_control).

% Rule: Jika ada pemain kunci absen DAN perbedaan ranking besar, maka disadvantage signifikan
disadvantage_signifikan :- 
    akar_penyebab(pemain_kunci_absen, man),
    ranking_fifa(indonesia, RankIndo),
    ranking_fifa(iraq, RankIraq),
    RankIndo - RankIraq > 50.

% --- B.4 RULES: Identifikasi Penyebab Kelemahan Strategi ---
% Rule: Kelemahan strategi jika ada masalah taktik DAN kebingungan operan
kelemahan_strategi :- 
    akar_penyebab(kurangnya_taktik_penyerangan, method),
    akar_penyebab(kebingungan_opsi_operan, method).

% --- B.5 RULES: Identifikasi Kelelahan Pemain ---
% Rule: Kelelahan pemain jika kurang fasilitas pemulihan DAN kondisi cuaca panas
kelelahan_pemain :- 
    akar_penyebab(kurangnya_fasilitas_pemulihan, material),
    akar_penyebab(kondisi_cuaca_panas_arab_saudi, environment).

% Rule: Kelelahan diperberat jika jadwal padat
kelelahan_parah :- 
    kelelahan_pemain,
    akar_penyebab(jadwal_padat_3_hari, environment).

% --- B.6 RULES: Analisis Performa vs Ekspektasi ---
% Rule: Performa di bawah standar jika shot banyak tapi tidak ada on target
performa_finishing_buruk :- 
    jumlah_shot(indonesia, Total),
    Total > 0,
    shot_on_target(indonesia, 0).

% Rule: Dominasi semu jika penguasaan bola hampir seimbang tapi tidak produktif
dominasi_semu :- 
    penguasaan_bola(indonesia, PossIndo),
    penguasaan_bola(iraq, PossIraq),
    abs(PossIndo - PossIraq) =< 5,
    shot_on_target(indonesia, 0).

% =================================================================
% BAGIAN C: RULE RANTAI 3+ LANGKAH (Chain of Reasoning)
% =================================================================

% --- C.1 RULE RANTAI: Analisis Kekalahan Komprehensif ---
% Step 1 (P → Q): Jika kelelahan parah, maka performa menurun
performa_menurun :- kelelahan_parah.

% Step 2 (Q → R): Jika performa menurun DAN kelemahan strategi, maka efektivitas_rendah
efektivitas_rendah :- 
    performa_menurun,
    kelemahan_strategi.

% Step 3 (R → S): Jika efektivitas rendah DAN masalah penyerangan kritis, maka kekalahan_tak_terelakkan
kekalahan_tak_terelakkan :- 
    efektivitas_rendah,
    masalah_penyerangan_kritis.

% Step 4 (S → T): Jika kekalahan tak terelakkan DAN disadvantage signifikan, maka analisis_kekalahan_lengkap
analisis_kekalahan_lengkap :- 
    kekalahan_tak_terelakkan,
    disadvantage_signifikan.

% --- C.2 RULE RANTAI ALTERNATIF: Dari Masalah ke Solusi ---
% P → Q: Masalah identifikasi
masalah_teridentifikasi :- 
    masalah_penyerangan_kritis,
    masalah_kontrol_permainan.

% Q → R: Kategorisasi berdasarkan severity
butuh_intervensi_mendesak :- 
    masalah_teridentifikasi,
    severity_critical(lemah_finishing).

% R → S: Rekomendasi strategis
butuh_revisi_total_strategi :- 
    butuh_intervensi_mendesak,
    kelemahan_strategi.

% =================================================================
% BAGIAN D: REKOMENDASI SOLUSI (Adaptasi dari Template)
% =================================================================

% --- D.1 SISTEM REKOMENDASI BERBASIS SEVERITY & KATEGORI ---

% KRITIS - MASALAH TEKNIS (Man/Player)
rekomendasi_solusi(Masalah, critical, man, 
    'URGENT: Lakukan pemusatan latihan intensif finishing dan shooting drill. 
    Rekrut striker naturalisasi berkualitas tinggi. Evaluasi coach specialized striker training.') :-
    severity_critical(Masalah),
    masalah_teknis(Masalah).

% KRITIS - MASALAH STRATEGIS (Method)
rekomendasi_solusi(Masalah, critical, method,
    'URGENT: Redesign formasi menjadi lebih menyerang (misal 4-2-3-1 atau 3-4-3). 
    Latih variasi serangan: counter-attack, build-up play, set-piece optimization. 
    Tunjuk analis taktik spesialis Asia Barat.') :-
    severity_critical(Masalah),
    masalah_strategis(Masalah).

% MODERATE - MASALAH EKSTERNAL (Environment)
rekomendasi_solusi(Masalah, moderate, environment,
    'MODERATE: Lakukan aklimatisasi 5-7 hari sebelum pertandingan di Arab Saudi. 
    Sediakan cooling system dan hidrasi optimal. Simulasi training di kondisi serupa.') :-
    severity_moderate(Masalah),
    masalah_eksternal(Masalah).

% MODERATE - MASALAH INFRASTRUKTUR (Material)
rekomendasi_solusi(Masalah, moderate, material,
    'MODERATE: Tingkatkan investasi sport science & recovery facility. 
    Bangun kerjasama dengan klub Eropa untuk player development. 
    Perkuat kedalaman skuad dengan naturalisasi terencana.') :-
    severity_moderate(Masalah),
    masalah_infrastruktur(Masalah).

% MINOR - SEMUA KATEGORI
rekomendasi_solusi(Masalah, minor, _, 
    'MINOR: Monitor dan evaluasi berkala. Perbaikan inkremental sudah cukup.') :-
    severity_minor(Masalah).

% --- D.2 REKOMENDASI SPESIFIK BERBASIS ANALISIS KEKALAHAN ---
rekomendasi_komprehensif(Kategori, Rekomendasi) :-
    Kategori = penyerangan,
    masalah_penyerangan_kritis,
    Rekomendasi = 'PRIORITAS TERTINGGI (Penyerangan):
    1. Rekrut striker alami dengan track record internasional (target: min 10 gol/musim di liga top)
    2. Intensifkan latihan finishing & decision making di box
    3. Implementasi shooting drill harian dengan variasi situasi
    4. Analisis video finishing Iraq & tim Asia top tier
    5. Evaluasi posisi false-nine atau dual-striker system'.

rekomendasi_komprehensif(Kategori, Rekomendasi) :-
    Kategori = taktik,
    kelemahan_strategi,
    Rekomendasi = 'PRIORITAS TINGGI (Taktik):
    1. Variasi formasi: siapkan Plan B (3-5-2) dan Plan C (4-4-2 diamond)
    2. Latih transisi cepat defense-to-attack (counter-pressing)
    3. Perbaiki ball progression dari defense ke attack third
    4. Workshop intensif pemahaman tactical flexibility
    5. Tunjuk assistant coach spesialis set-piece & dead ball situation'.

rekomendasi_komprehensif(Kategori, Rekomendasi) :-
    Kategori = fisik,
    kelelahan_parah,
    Rekomendasi = 'PRIORITAS TINGGI (Fisik & Recovery):
    1. Terapkan periodization training modern (taper phase sebelum match)
    2. Upgrade fasilitas: cryotherapy, hydrotherapy, compression therapy
    3. Rekrut sport scientist & nutritionist berkualifikasi internasional
    4. Monitoring GPS data & load management per pemain
    5. Acclimatization protocol untuk pertandingan di Timur Tengah (min 5 hari)'.

rekomendasi_komprehensif(Kategori, Rekomendasi) :-
    Kategori = mental,
    disadvantage_signifikan,
    Rekomendasi = 'PRIORITAS MENENGAH (Mental & Psikologis):
    1. Rekrut sport psychologist untuk mental toughness training
    2. Simulasi pertandingan pressure cooker (friendly vs tim kuat)
    3. Team building intensif untuk chemistry building
    4. Edukasi pemain tentang gap analysis realitis Indonesia vs top Asia
    5. Fokus pada process-oriented mindset, bukan result-oriented'.

% --- D.3 UTILITY RULES: Helper Functions ---

% Mencari semua penyebab dalam kategori tertentu
cari_penyebab_kategori(Kategori, Penyebab) :- 
    akar_penyebab(Penyebab, Kategori).

% Menghitung jumlah masalah kritis
hitung_masalah_kritis(Total) :- 
    findall(M, severity_critical(M), List),
    length(List, Total).

% Diagnosa lengkap dengan rekomendasi
diagnosa_lengkap(Masalah, Severity, Kategori, Rekomendasi) :-
    akar_penyebab(Masalah, Kategori),
    (severity_critical(Masalah) -> Severity = critical
    ; severity_moderate(Masalah) -> Severity = moderate
    ; severity_minor(Masalah) -> Severity = minor),
    rekomendasi_solusi(Masalah, Severity, Kategori, Rekomendasi).

% Cek apakah tim memiliki kelemahan fundamental
kelemahan_fundamental :- 
    masalah_penyerangan_kritis,
    kelemahan_strategi,
    disadvantage_signifikan.

% Prioritas perbaikan (1 = tertinggi)
prioritas_perbaikan(Masalah, 1) :- 
    severity_critical(Masalah),
    masalah_strategis(Masalah).

prioritas_perbaikan(Masalah, 2) :- 
    severity_critical(Masalah),
    masalah_teknis(Masalah).

prioritas_perbaikan(Masalah, 3) :- 
    severity_moderate(Masalah).

prioritas_perbaikan(Masalah, 4) :- 
    severity_minor(Masalah).

% =================================================================
% BAGIAN E: QUERY EXAMPLES (Untuk Testing di PySwip)
% =================================================================

% Contoh Query yang dapat dijalankan:
% 
% 1. Cek kekalahan tak terelakkan (rantai 4 langkah):
%    ?- analisis_kekalahan_lengkap.
%
% 2. Lihat semua masalah kritis:
%    ?- severity_critical(X).
%
% 3. Cek masalah penyerangan:
%    ?- masalah_penyerangan_kritis.
%
% 4. Dapatkan rekomendasi untuk masalah tertentu:
%    ?- diagnosa_lengkap(lemah_finishing, Sev, Kat, Rek).
%
% 5. Cek kelemahan fundamental:
%    ?- kelemahan_fundamental.
%
% 6. Lihat semua akar penyebab kategori 'method':
%    ?- cari_penyebab_kategori(method, X).
%
% 7. Hitung total masalah kritis:
%    ?- hitung_masalah_kritis(N).
%
% 8. Cek prioritas perbaikan masalah:
%    ?- prioritas_perbaikan(lemah_finishing, P).
%
% 9. Dapatkan rekomendasi komprehensif:
%    ?- rekomendasi_komprehensif(penyerangan, R).
%
% 10. Cek apakah ada kelelahan parah:
%     ?- kelelahan_parah.

% =================================================================
% END OF KNOWLEDGE BASE
% =================================================================