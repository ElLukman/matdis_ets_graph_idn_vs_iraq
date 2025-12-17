% =================================================================
% FILE: prolog_kb_dayanlagi.pl
% Knowledge Base - Analisis Kekalahan Timnas Indonesia vs Iraq
% Topik: Sistem Inferensi Kebijakan (FOL)
% Data: Lengkap sesuai Laporan (Passing 430, Fishbone, dll)
% =================================================================

% =================================================================
% BAGIAN A: FACTS (FAKTA)
% =================================================================

% --- A.1 PROPOSISI ---
pertandingan_selesai.
venue_netral.
hasil_imbang_tidak_tercapai.

% --- A.2 DATA PERTANDINGAN ---
pertandingan(indonesia, iraq, '2025-10-12').
lokasi(pertandingan_ini, jeddah, saudi_arabia).
skor_akhir(indonesia, 0).
skor_akhir(iraq, 1).
stadion(king_abdullah_sports_city, kapasitas(62241)).
pencetak_gol(zidane_iqbal, iraq, menit(76)).
wasit_utama(muhammad_taqi, qatar).

% --- A.3 PROFIL TIM ---
pelatih(indonesia, patrick_kluivert).
pelatih(iraq, graham_arnold).
ranking_fifa(indonesia, 118).
ranking_fifa(iraq, 58).
formasi(indonesia, '4-3-3').
formasi(iraq, '4-2-3-1').

% --- A.4 DATA PEMAIN (Lengkap) ---
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
pemain_data(shayne_pattynama, 22, bek_kiri, belanda, sub).

% --- A.5 ATRIBUT PEMAIN ---
pemain_naturalisasi(jay_idzes).
pemain_naturalisasi(thom_haye).
pemain_naturalisasi(calvin_verdonk).
pemain_naturalisasi(sandy_walsh).
pemain_naturalisasi(rafael_struick).
pemain_naturalisasi(ragnar_oratmangoen).
pemain_naturalisasi(nathan_tjoe_a_on).
pemain_naturalisasi(justin_hubner).
pemain_naturalisasi(elkan_baggott).

kapten(indonesia, jay_idzes).
kapten(iraq, ali_jasim).

% --- A.6 STATISTIK PEMAIN (Passing 430, dll) ---
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

statistik_pemain(shayne_pattynama, tackle, 6, kali).

akurasi_passing(jay_idzes, 92, persen).
akurasi_passing(thom_haye, 88, persen).
akurasi_passing(marselino_ferdinan, 85, persen).

% --- A.7 STATISTIK TIM (Grouped) ---
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

% --- A.8 AKAR PENYEBAB (Fishbone) ---
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

akar_penyebab(xg_rendah_031, measurement).

% --- A.9 SEVERITY SCORE ---
tingkat_kekritisan(lemah_finishing, 9).
tingkat_kekritisan(pressing_tidak_efektif, 8).
tingkat_kekritisan(kebingungan_opsi_operan, 8).
tingkat_kekritisan(gagal_breakdown_defense_iraq, 9).
tingkat_kekritisan(kurangnya_pengalaman_pemain, 7).
tingkat_kekritisan(pemain_kunci_absen, 7).
tingkat_kekritisan(kondisi_cuaca_panas_arab_saudi, 6).
tingkat_kekritisan(substitusi_kurang_efektif, 5).

% --- A.10 LAINNYA ---
kekuatan_lawan(iraq, high_pressing_intensity).
kekuatan_lawan(iraq, physical_dominance).
kekuatan_lawan(iraq, experienced_core_players).
kekuatan_lawan(iraq, tactical_discipline).
kekuatan_lawan(iraq, midfield_control).

operan_sukses(jay_idzes, marselino_ferdinan, 45).
operan_sukses(jay_idzes, thom_haye, 38).
operan_sukses(thom_haye, marselino_ferdinan, 32).
operan_sukses(marselino_ferdinan, rafael_struick, 28).
operan_sukses(calvin_verdonk, marselino_ferdinan, 25).

status_pemain(maarten_paes, absen_akumulasi_kartu).
status_pemain(asnawi_mangkualam, cedera_lutut).
status_pemain(rachmat_irianto, tidak_dipanggil).

% =================================================================
% BAGIAN B: RULES DASAR
% =================================================================

% B.1 Klasifikasi Severity
severity_minor(Masalah) :- tingkat_kekritisan(Masalah, Score), Score < 4.
severity_moderate(Masalah) :- tingkat_kekritisan(Masalah, Score), Score >= 4, Score =< 7.
severity_critical(Masalah) :- tingkat_kekritisan(Masalah, Score), Score > 7.

% B.2 Identifikasi Kategori
masalah_teknis(Masalah) :- akar_penyebab(Masalah, man).
masalah_strategis(Masalah) :- akar_penyebab(Masalah, method).
masalah_eksternal(Masalah) :- akar_penyebab(Masalah, environment).
masalah_infrastruktur(Masalah) :- akar_penyebab(Masalah, material).

% B.3 Pemain Kunci (Passing > 350)
pemain_kunci(Pemain) :- 
    statistik_pemain(Pemain, passing, Jumlah, total_operan), Jumlah > 350.

% B.4 Hub Permainan (Tombol 3)
hub_permainan(Pemain) :- 
    pemain_kunci(Pemain),
    akurasi_passing(Pemain, Akurasi, persen), Akurasi > 90.

% B.5 Pilar Pertahanan (Tackle >= 5)
pilar_pertahanan(Pemain) :- 
    statistik_pemain(Pemain, tackle, Jumlah, kali), Jumlah >= 5.

% B.6 Penyerang Aktif
penyerang_aktif(Pemain) :- 
    statistik_pemain(Pemain, shot, Jumlah, tembakan), Jumlah >= 2.

% B.7 Pemain Kreatif
pemain_kreatif(Pemain) :- statistik_pemain(Pemain, key_pass, Jumlah, operan_kunci), Jumlah >= 4.
pemain_kreatif(Pemain) :- statistik_pemain(Pemain, dribble, Jumlah, sukses), Jumlah >= 6.

% B.8 Masalah Penyerangan Kritis
masalah_penyerangan_kritis :- 
    severity_critical(lemah_finishing),
    statistik_tim(indonesia, shots_on_target, 0).

% B.9 Masalah Kontrol Permainan
masalah_kontrol_permainan :- 
    severity_critical(pressing_tidak_efektif),
    kekuatan_lawan(iraq, midfield_control).

% B.10 Gap Kualitas
gap_kualitas_signifikan :- 
    ranking_fifa(indonesia, R1), ranking_fifa(iraq, R2), R1 - R2 > 50.

% B.11 Kelemahan Strategi
kelemahan_strategi :- 
    akar_penyebab(kurangnya_taktik_penyerangan, method),
    akar_penyebab(kebingungan_opsi_operan, method).

% B.12 Kelelahan Pemain
kelelahan_pemain :- 
    akar_penyebab(kurangnya_fasilitas_pemulihan, material),
    akar_penyebab(kondisi_cuaca_panas_arab_saudi, environment).

% B.13 Kelelahan Parah (Step 1 Rantai)
% Rule ini menghubungkan fakta agar trace Step 1 berhasil
kelelahan_parah :- 
    kelelahan_pemain,
    akar_penyebab(jadwal_padat_3_hari, environment).

% B.14 Performa Buruk
performa_finishing_buruk :- 
    statistik_tim(indonesia, total_shots, Total), Total > 0,
    statistik_tim(indonesia, shots_on_target, 0).

% B.15 Dominasi Semu
dominasi_semu :- 
    statistik_tim(indonesia, possession, P1), statistik_tim(iraq, possession, P2),
    abs(P1 - P2) =< 5,
    statistik_tim(indonesia, shots_on_target, 0).

% B.16 Disadvantage
disadvantage_signifikan :- 
    akar_penyebab(pemain_kunci_absen, man),
    gap_kualitas_signifikan.

% =================================================================
% BAGIAN C: RULES RANTAI (CHAINING)
% =================================================================

% C.1 Analisis Kekalahan (4 Langkah - Tombol 5)
% Step 2 Trace
performa_menurun :- kelelahan_parah.

% Step 3 Trace
efektivitas_rendah :- 
    performa_menurun,
    kelemahan_strategi.

% Step 4 Trace (Final)
kekalahan_tak_terelakkan :- 
    efektivitas_rendah,
    masalah_penyerangan_kritis.

analisis_kekalahan_lengkap :- 
    kekalahan_tak_terelakkan,
    disadvantage_signifikan.

% C.2 Pemain Vital (Tombol 4)
pemain_all_around(Pemain) :- 
    hub_permainan(Pemain), 
    pilar_pertahanan(Pemain).

pemain_vital(Pemain) :- 
    pemain_all_around(Pemain), 
    penyerang_aktif(Pemain).

% =================================================================
% BAGIAN D: REKOMENDASI SOLUSI (EXPERT SYSTEM)
% =================================================================

% D.1 Mapping Solusi (Agar Tombol 7 Berhasil)
rekomendasi_solusi(lemah_finishing, 'URGENT: Drill finishing xG rendah & rekrut pelatih striker khusus.').
rekomendasi_solusi(kebingungan_opsi_operan, 'TACTICAL: Latihan rondo intensitas tinggi.').
rekomendasi_solusi(kondisi_cuaca_panas_arab_saudi, 'PHYSICAL: Aklimatisasi H-7 dan terapi ice bath.').

% D.2 Diagnosa Lengkap (Tombol 7)
diagnosa_lengkap(Masalah, Severity, Kategori, Solusi) :-
    akar_penyebab(Masalah, Kategori),
    (severity_critical(Masalah) -> Severity = critical
    ; severity_moderate(Masalah) -> Severity = moderate
    ; severity_minor(Masalah) -> Severity = minor),
    rekomendasi_solusi(Masalah, Solusi).