% =================================================================
% FILE: prolog_kb.pl
% Knowledge Base Logika Orde Pertama (FOL) untuk Analisis Performa Timnas Indonesia
% =================================================================

% --- TEMA: ANALISIS FREKUENSI PASSING, SHOOTING, DAN TACKLE WON ---
% --- TIMNAS INDONESIA VS IRAQ 4TH ROUND WORLD CUP QUALIFIERS ---

% -----------------------------------------------------------------
% 1. DEFINISI FACTS (8 Facts / Proposisi Dasar)
% -----------------------------------------------------------------

% Fakta pemain aktif dalam pertandingan
pemain_aktif(pemain_17).
pemain_aktif(pemain_22).
pemain_aktif(pemain_13).
pemain_aktif(pemain_15).
pemain_aktif(pemain_21).

% Fakta passing tinggi (>50 passing berdasarkan adjacency list)
passing_tinggi(pemain_17).  % Pemain paling sering passing

% Fakta shooting aktif (>1 shot berdasarkan data shooting)
shooting_aktif(pemain_17).  % 2 shots
shooting_aktif(pemain_13).  % 2 shots

% Fakta tackle kuat (>=5 tackle won)
tackle_kuat(pemain_17).  % 6 tackle
tackle_kuat(pemain_22).  % 6 tackle
tackle_kuat(pemain_15).  % 5 tackle

% Fakta tambahan untuk inferensi
posisi_tengah(pemain_17).
posisi_depan(pemain_13).

% -----------------------------------------------------------------
% 2. DEFINISI RULES (5 Rules / Implikasi FOL)
% -----------------------------------------------------------------

% Rule 1: Jika pemain memiliki passing tinggi, maka dia adalah hub permainan
% FOL: ∀X (passing_tinggi(X) → hub_permainan(X))
hub_permainan(X) :- passing_tinggi(X).

% Rule 2: Jika pemain adalah hub permainan DAN memiliki tackle kuat, 
%         maka dia adalah pemain kunci (rantai 2 langkah dari Rule 1)
% FOL: ∀X (hub_permainan(X) ∧ tackle_kuat(X) → pemain_kunci(X))
pemain_kunci(X) :- 
    hub_permainan(X), 
    tackle_kuat(X).

% Rule 3: Jika pemain shooting aktif DAN pemain aktif, 
%         maka dia adalah penyerang efektif
% FOL: ∀X (shooting_aktif(X) ∧ pemain_aktif(X) → penyerang_efektif(X))
penyerang_efektif(X) :- 
    shooting_aktif(X), 
    pemain_aktif(X).

% Rule 4: Jika pemain adalah pemain kunci DAN shooting aktif, 
%         maka dia adalah pemain vital (rantai 3 langkah)
% FOL: ∀X (pemain_kunci(X) ∧ shooting_aktif(X) → pemain_vital(X))
pemain_vital(X) :- 
    pemain_kunci(X), 
    shooting_aktif(X).

% Rule 5: Jika pemain adalah hub permainan DAN penyerang efektif,
%         maka dia adalah pemain all-around
% FOL: ∀X (hub_permainan(X) ∧ penyerang_efektif(X) → pemain_all_around(X))
pemain_all_around(X) :- 
    hub_permainan(X), 
    penyerang_efektif(X).

% -----------------------------------------------------------------
% 3. RULES TAMBAHAN UNTUK ANALISIS MENDALAM
% -----------------------------------------------------------------

% Rule 6: Pemain dengan tackle kuat adalah pilar pertahanan
pilar_pertahanan(X) :- tackle_kuat(X).

% Rule 7: Jika pemain adalah pemain vital, maka butuh proteksi khusus
butuh_proteksi(X) :- pemain_vital(X).

% Rule 8: Rekomendasi strategi berdasarkan karakteristik pemain
strategi_optimal(bertahan_dan_serang, X) :- 
    pemain_all_around(X).

strategi_optimal(fokus_distribusi, X) :- 
    hub_permainan(X), 
    \+ shooting_aktif(X).

% -----------------------------------------------------------------
% FAKTA SPESIFIK UNTUK UJI RANTAI INFERENSI 3 LANGKAH
% -----------------------------------------------------------------
% Fakta Spesifik: passing_tinggi(pemain_17)
% Rantai Inferensi:
% 1. passing_tinggi(pemain_17) → hub_permainan(pemain_17)  [Rule 1]
% 2. hub_permainan(pemain_17) ∧ tackle_kuat(pemain_17) → pemain_kunci(pemain_17)  [Rule 2]
% 3. pemain_kunci(pemain_17) ∧ shooting_aktif(pemain_17) → pemain_vital(pemain_17)  [Rule 4]
% Kesimpulan: pemain_vital(pemain_17)