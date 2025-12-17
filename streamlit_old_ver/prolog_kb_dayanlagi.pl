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
% KONSEP LOGIKA FORMAL:
% - PROPOSISI: Pernyataan boolean (arity 0)
% - PREDIKAT UNARY: Predikat dengan 1 argumen
% - PREDIKAT BINARY: Predikat dengan 2 argumen
% - PREDIKAT TERNARY: Predikat dengan 3 argumen
% - PREDIKAT N-ARY: Predikat dengan 4+ argumen (struktur kompleks)
% - KONSTANTA: jay_idzes, marselino_ferdinan, 430, iraq, indonesia
% - VARIABEL: X, Y, Pemain, Jumlah, Kategori (digunakan dalam rules)
% =================================================================

% =================================================================
% BAGIAN A: FACTS - Minimal 15 Facts (STRUKTUR KOMPLEKS)
% =================================================================

% --- A.1 PROPOSISI (Arity 0) - Pernyataan Boolean ---
pertandingan_selesai.
venue_netral.
hasil_imbang_tidak_tercapai.

% --- A.2 FACTS: Data Pertandingan (PREDIKAT BINARY & TERNARY) ---
pertandingan(indonesia, iraq, '2025-10-12').
lokasi(pertandingan_ini, jeddah, saudi_arabia).
skor_akhir(indonesia, 0).
skor_akhir(iraq, 1).
stadion(king_abdullah_sports_city, kapasitas(62241)).
pencetak_gol(zidane_iqbal, iraq, menit(76)).
wasit_utama(muhammad_taqi, qatar).

% --- A.3 FACTS: Profil Tim (PREDIKAT BINARY) ---
pelatih(indonesia, patrick_kluivert).
pelatih(iraq, graham_arnold).
ranking_fifa(indonesia, 118).
ranking_fifa(iraq, 58).
formasi(indonesia, '4-3-3').
formasi(iraq, '4-2-3-1').

% --- A.4 FACTS: Data Pemain Indonesia (PREDIKAT N-ARY dengan STRUKTUR KOMPLEKS) ---
% Format: pemain_data(Nama, Nomor, Posisi, Negara_Asal, Status)
pemain_data(jay_idzes, 6, bek_tengah, belanda, starter).
pemain_data(thom_haye, 8, gelandang_tengah, belanda, starter).
pemain_data(calvin_verdonk, 5, bek_kiri, belanda, starter).
pemain_data(sandy_walsh, 2, bek_kanan, belanda, starter).
pemain_data(rafael_struick, 17, penyerang, belanda, starter).
pemain_data(ragnar_oratmangoen, 11, sayap_kanan, norwegia, starter).
pemain_data(marselino_ferdinan, 10, gelandang_serang, indonesia, starter).
pemain_data(nathan_tjoe_a_on, 13, gelandang, belanda, starter).
pemain_data(justin_hubner, 15, gelandang_bertahan, australia, starter).
pemain_data(elkan_baggott, 4, bek_tengah, inggris, cadangan).
pemain_data(rizky_ridho, 3, bek_tengah, indonesia, cadangan).

% Pemain Naturalisasi (PREDIKAT UNARY)
pemain_naturalisasi(jay_idzes).
pemain_naturalisasi(thom_haye).
pemain_naturalisasi(calvin_verdonk).
pemain_naturalisasi(sandy_walsh).
pemain_naturalisasi(rafael_struick).
pemain_naturalisasi(ragnar_oratmangoen).
pemain_naturalisasi(nathan_tjoe_a_on).
pemain_naturalisasi(justin_hubner).
pemain_naturalisasi(elkan_baggott).

% Kapten Tim (PREDIKAT BINARY)
kapten(indonesia, jay_idzes).
kapten(iraq, ali_jasim).

% --- A.5 FACTS: Statistik Pemain (PREDIKAT N-ARY - 4 Argumen) ---
% Format: statistik_pemain(Nama, Kategori, Jumlah, Unit)
statistik_pemain(jay_idzes, passing, 430, total_operan).
statistik_pemain(jay_idzes, tackle, 6, kali).
statistik_pemain(jay_idzes, shot, 2, tembakan).
statistik_pemain(jay_idzes, card, 1, kuning).

statistik_pemain(thom_haye, passing, 380, total_operan).
statistik_pemain(thom_haye, tackle, 4, kali).
statistik_pemain(thom_haye, shot, 1, tembakan).

statistik_pemain(marselino_ferdinan, passing, 320, total_operan).
statistik_pemain(marselino_ferdinan, dribble, 8, sukses).
statistik_pemain(marselino_ferdinan, shot, 3, tembakan).
statistik_pemain(marselino_ferdinan, key_pass, 5, operan_kunci).

statistik_pemain(rafael_struick, shot, 2, tembakan).
statistik_pemain(rafael_struick, passing, 180, total_operan).

statistik_pemain(justin_hubner, tackle, 5, kali).
statistik_pemain(justin_hubner, interception, 4, kali).

statistik_pemain(calvin_verdonk, tackle, 3, kali).
statistik_pemain(calvin_verdonk, passing, 290, total_operan).

% Statistik Akurasi (PREDIKAT TERNARY)
akurasi_passing(jay_idzes, 92, persen).
akurasi_passing(thom_haye, 88, persen).
akurasi_passing(marselino_ferdinan, 85, persen).

% --- A.6 FACTS: Statistik Tim (PREDIKAT TERNARY) ---
statistik_tim(indonesia, possession, 48).
statistik_tim(indonesia, total_shots, 5).
statistik_tim(indonesia, shots_on_target, 0).
statistik_tim(indonesia, corners, 3).
statistik_tim(indonesia, fouls, 12).
statistik_tim(indonesia, yellow_cards, 2).
statistik_tim(indonesia, pass_accuracy, 85).

statistik_tim(iraq, possession, 52).
statistik_tim(iraq, total_shots, 8).
statistik_tim(iraq, shots_on_target, 3).
statistik_tim(iraq, corners, 5).
statistik_tim(iraq, fouls, 14).
statistik_tim(iraq, yellow_cards, 2).
statistik_tim(iraq, red_cards, 1).

% --- A.7 FACTS: Akar Penyebab (PREDIKAT BINARY dengan KATEGORI) ---
% Kategori Fishbone: man, method, environment, material
akar_penyebab(lemah_finishing, man).
akar_penyebab(kurangnya_pengalaman_pemain, man).
akar_penyebab(kurangnya_konsentrasi_pemain, man).
akar_penyebab(pemain_kunci_absen, man).
akar_penyebab(perbedaan_kualitas_pemain, man).

akar_penyebab(kurangnya_taktik_penyerangan, method).
akar_penyebab(kebingungan_opsi_operan, method).
akar_penyebab(substitusi_kurang_efektif, method).
akar_penyebab(pressing_tidak_efektif, method).
akar_penyebab(gagal_breakdown_defense_iraq, method).

akar_penyebab(kondisi_cuaca_panas_arab_saudi, environment).
akar_penyebab(kondisi_lapangan_cepat, environment).
akar_penyebab(venue_netral_menguntungkan_iraq, environment).
akar_penyebab(jadwal_padat_3_hari, environment).

akar_penyebab(kurangnya_fasilitas_pemulihan, material).
akar_penyebab(keterbatasan_kedalaman_skuad, material).

% --- A.8 FACTS: Tingkat Kekritisan (PREDIKAT BINARY) ---
tingkat_kekritisan(lemah_finishing, 9).
tingkat_kekritisan(pressing_tidak_efektif, 8).
tingkat_kekritisan(kebingungan_opsi_operan, 8).
tingkat_kekritisan(gagal_breakdown_defense_iraq, 9).
tingkat_kekritisan(kurangnya_pengalaman_pemain, 7).
tingkat_kekritisan(pemain_kunci_absen, 7).
tingkat_kekritisan(kondisi_cuaca_panas_arab_saudi, 6).
tingkat_kekritisan(substitusi_kurang_efektif, 5).

% --- A.9 FACTS: Kekuatan Lawan Iraq (PREDIKAT BINARY) ---
kekuatan_lawan(iraq, high_pressing_intensity).
kekuatan_lawan(iraq, physical_dominance).
kekuatan_lawan(iraq, experienced_core_players).
kekuatan_lawan(iraq, tactical_discipline).
kekuatan_lawan(iraq, midfield_control).

% --- A.10 FACTS: Relasi Operan Antar Pemain (PREDIKAT TERNARY) ---
operan_sukses(jay_idzes, marselino_ferdinan, 45).
operan_sukses(jay_idzes, thom_haye, 38).
operan_sukses(thom_haye, marselino_ferdinan, 32).
operan_sukses(marselino_ferdinan, rafael_struick, 28).
operan_sukses(calvin_verdonk, marselino_ferdinan, 25).

% --- A.11 FACTS: Pemain Absen/Cedera (PREDIKAT BINARY) ---
status_pemain(maarten_paes, absen_akumulasi_kartu).
status_pemain(asnawi_mangkualam, cedera_lutut).
status_pemain(rachmat_irianto, tidak_dipanggil).

% =================================================================
% BAGIAN B: RULES - Minimal 8 Rules (DENGAN VARIABEL)
% =================================================================

% --- B.1 RULE: Klasifikasi Tingkat Kritis (UNARY PREDICATE) ---
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

% --- B.2 RULE: Identifikasi Kategori Masalah ---
masalah_teknis(Masalah) :- 
    akar_penyebab(Masalah, man).

masalah_strategis(Masalah) :- 
    akar_penyebab(Masalah, method).

masalah_eksternal(Masalah) :- 
    akar_penyebab(Masalah, environment).

masalah_infrastruktur(Masalah) :- 
    akar_penyebab(Masalah, material).

% --- B.3 RULE: Pemain Kunci (BINARY - Berdasarkan Passing) ---
% Jika pemain passing > 350, maka pemain kunci
pemain_kunci(Pemain) :- 
    statistik_pemain(Pemain, passing, Jumlah, total_operan),
    Jumlah > 350.

% --- B.4 RULE: Hub Permainan (UNARY - Pemain dengan Passing Tertinggi) ---
% Jika pemain adalah pemain kunci DAN akurasi > 90%, maka hub permainan
hub_permainan(Pemain) :- 
    pemain_kunci(Pemain),
    akurasi_passing(Pemain, Akurasi, persen),
    Akurasi > 90.

% --- B.5 RULE: Pilar Pertahanan (BINARY - Berdasarkan Tackle) ---
% Jika tackle >= 5, maka pilar pertahanan
pilar_pertahanan(Pemain) :- 
    statistik_pemain(Pemain, tackle, Jumlah, kali),
    Jumlah >= 5.

% --- B.6 RULE: Penyerang Aktif (BINARY - Berdasarkan Shot) ---
% Jika shot >= 2, maka penyerang aktif
penyerang_aktif(Pemain) :- 
    statistik_pemain(Pemain, shot, Jumlah, tembakan),
    Jumlah >= 2.

% --- B.7 RULE: Pemain Kreatif (TERNARY - Key Pass & Dribble) ---
% Jika key_pass >= 4 ATAU dribble >= 6, maka pemain kreatif
pemain_kreatif(Pemain) :- 
    statistik_pemain(Pemain, key_pass, Jumlah, operan_kunci),
    Jumlah >= 4.

pemain_kreatif(Pemain) :- 
    statistik_pemain(Pemain, dribble, Jumlah, sukses),
    Jumlah >= 6.

% --- B.8 RULE: Masalah Penyerangan Kritis (COMPLEX RULE) ---
% Jika lemah finishing KRITIS DAN shots on target = 0
masalah_penyerangan_kritis :- 
    severity_critical(lemah_finishing),
    statistik_tim(indonesia, shots_on_target, 0).

% --- B.9 RULE: Masalah Kontrol Permainan (COMPLEX RULE) ---
% Jika pressing tidak efektif KRITIS DAN Iraq kontrol midfield
masalah_kontrol_permainan :- 
    severity_critical(pressing_tidak_efektif),
    kekuatan_lawan(iraq, midfield_control).

% --- B.10 RULE: Gap Kualitas Signifikan (BINARY dengan ARITMATIKA) ---
% Jika selisih ranking FIFA > 50
gap_kualitas_signifikan :- 
    ranking_fifa(indonesia, RankIndo),
    ranking_fifa(iraq, RankIraq),
    RankIndo - RankIraq > 50.

% --- B.11 RULE: Kelemahan Strategi (CONJUNCTION) ---
% Jika ada masalah taktik DAN kebingungan operan
kelemahan_strategi :- 
    akar_penyebab(kurangnya_taktik_penyerangan, method),
    akar_penyebab(kebingungan_opsi_operan, method).

% --- B.12 RULE: Kelelahan Pemain (CONJUNCTION) ---
% Jika kurang fasilitas pemulihan DAN kondisi cuaca panas
kelelahan_pemain :- 
    akar_penyebab(kurangnya_fasilitas_pemulihan, material),
    akar_penyebab(kondisi_cuaca_panas_arab_saudi, environment).

% --- B.13 RULE: Kelelahan Parah (CHAINING) ---
kelelahan_parah :- 
    kelelahan_pemain,
    akar_penyebab(jadwal_padat_3_hari, environment).

% --- B.14 RULE: Performa di Bawah Standar ---
performa_finishing_buruk :- 
    statistik_tim(indonesia, total_shots, Total),
    Total > 0,
    statistik_tim(indonesia, shots_on_target, 0).

% --- B.15 RULE: Dominasi Semu (COMPLEX ARITHMETIC) ---
dominasi_semu :- 
    statistik_tim(indonesia, possession, PossIndo),
    statistik_tim(iraq, possession, PossIraq),
    abs(PossIndo - PossIraq) =< 5,
    statistik_tim(indonesia, shots_on_target, 0).

% --- B.16 RULE: Disadvantage Signifikan (COMPLEX RULE) ---
disadvantage_signifikan :- 
    akar_penyebab(pemain_kunci_absen, man),
    gap_kualitas_signifikan.

% =================================================================
% BAGIAN C: RULE RANTAI 3+ LANGKAH (Chain of Reasoning)
% =================================================================

% --- C.1 RANTAI 4 LANGKAH: Analisis Kekalahan Komprehensif ---
% LANGKAH 1 (P → Q): Jika kelelahan parah, maka performa menurun
performa_menurun :- kelelahan_parah.

% LANGKAH 2 (Q → R): Jika performa menurun DAN kelemahan strategi, maka efektivitas rendah
efektivitas_rendah :- 
    performa_menurun,
    kelemahan_strategi.

% LANGKAH 3 (R → S): Jika efektivitas rendah DAN masalah penyerangan kritis, maka kekalahan tak terelakkan
kekalahan_tak_terelakkan :- 
    efektivitas_rendah,
    masalah_penyerangan_kritis.

% LANGKAH 4 (S → T): Jika kekalahan tak terelakkan DAN disadvantage signifikan, maka analisis kekalahan lengkap
analisis_kekalahan_lengkap :- 
    kekalahan_tak_terelakkan,
    disadvantage_signifikan.

% --- C.2 RANTAI 3 LANGKAH: Dari Masalah ke Solusi ---
% LANGKAH 1 (P → Q): Identifikasi masalah
masalah_teridentifikasi :- 
    masalah_penyerangan_kritis,
    masalah_kontrol_permainan.

% LANGKAH 2 (Q → R): Kategorisasi berdasarkan severity
butuh_intervensi_mendesak :- 
    masalah_teridentifikasi,
    severity_critical(lemah_finishing).

% LANGKAH 3 (R → S): Rekomendasi strategis
butuh_revisi_total_strategi :- 
    butuh_intervensi_mendesak,
    kelemahan_strategi.

% --- C.3 RANTAI 3 LANGKAH ALTERNATIF: Analisis Pemain Vital ---
% LANGKAH 1: Pemain dengan passing tinggi adalah hub permainan
% (sudah ada di rule B.4: hub_permainan)

% LANGKAH 2: Hub permainan yang juga pilar pertahanan adalah pemain_all_around
pemain_all_around(Pemain) :-
    hub_permainan(Pemain),
    pilar_pertahanan(Pemain).

% LANGKAH 3: Pemain all around yang juga penyerang aktif adalah pemain_vital
pemain_vital(Pemain) :-
    pemain_all_around(Pemain),
    penyerang_aktif(Pemain).

% =================================================================
% BAGIAN D: REKOMENDASI SOLUSI (Adaptasi Template)
% =================================================================

% --- D.1 SISTEM REKOMENDASI BERBASIS SEVERITY & KATEGORI ---
rekomendasi_solusi(Masalah, critical, man, 
    'URGENT: Lakukan pemusatan latihan intensif finishing dan shooting drill. Rekrut striker naturalisasi berkualitas tinggi. Evaluasi coach specialized striker training.') :-
    severity_critical(Masalah),
    masalah_teknis(Masalah).

rekomendasi_solusi(Masalah, critical, method,
    'URGENT: Redesign formasi menjadi lebih menyerang (misal 4-2-3-1 atau 3-4-3). Latih variasi serangan: counter-attack, build-up play, set-piece optimization. Tunjuk analis taktik spesialis Asia Barat.') :-
    severity_critical(Masalah),
    masalah_strategis(Masalah).

rekomendasi_solusi(Masalah, moderate, environment,
    'MODERATE: Lakukan aklimatisasi 5-7 hari sebelum pertandingan di Arab Saudi. Sediakan cooling system dan hidrasi optimal. Simulasi training di kondisi serupa.') :-
    severity_moderate(Masalah),
    masalah_eksternal(Masalah).

rekomendasi_solusi(Masalah, moderate, material,
    'MODERATE: Tingkatkan investasi sport science & recovery facility. Bangun kerjasama dengan klub Eropa untuk player development. Perkuat kedalaman skuad dengan naturalisasi terencana.') :-
    severity_moderate(Masalah),
    masalah_infrastruktur(Masalah).

rekomendasi_solusi(Masalah, minor, _, 
    'MINOR: Monitor dan evaluasi berkala. Perbaikan inkremental sudah cukup.') :-
    severity_minor(Masalah).

% --- D.2 UTILITY RULES ---
% Mencari semua penyebab dalam kategori tertentu
cari_penyebab_kategori(Kategori, Penyebab) :- 
    akar_penyebab(Penyebab, Kategori).

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

% =================================================================
% QUERY EXAMPLES (Untuk Testing)
% =================================================================
% 1. ?- pemain_kunci(X).
% 2. ?- hub_permainan(X).
% 3. ?- pemain_vital(X).
% 4. ?- masalah_penyerangan_kritis.
% 5. ?- analisis_kekalahan_lengkap.
% 6. ?- statistik_pemain(jay_idzes, passing, X, total_operan).
% 7. ?- operan_sukses(jay_idzes, X, Y).
% 8. ?- butuh_revisi_total_strategi.
% =================================================================