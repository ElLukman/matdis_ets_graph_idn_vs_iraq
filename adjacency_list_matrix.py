import pandas as pd
from collections import Counter

# ======================
# 1️⃣ Baca data CSV
# ======================
df = pd.read_csv("Matdis-Indonesia-Iraq - Sheet1.csv")

# ======================
# 2️⃣ Kumpulkan semua edges dari berbagai kolom
# ======================
edges = []

# ----- PASS -----
for value in df["pass"].dropna():
    players = [x.strip() for x in str(value).split(",") if x.strip().isdigit()]
    for i in range(len(players) - 1):
        edges.append((players[i], players[i + 1]))
    # Tambahkan LOSS ke pemain terakhir
    if len(players) > 0:
        edges.append((players[-1], "LOSS"))

# ----- SHOOT (ke GOAL) -----
if "shoot" in df.columns:
    for value in df["shoot"].dropna():
        shooters = [x.strip() for x in str(value).split(",") if x.strip().isdigit()]
        for s in shooters:
            edges.append((s, "GOAL"))

# ----- TACKLE (antar pemain) -----
if "tackle" in df.columns:
    for value in df["tackle"].dropna():
        tacklers = [x.strip() for x in str(value).split(",") if x.strip().isdigit()]
        for i in range(len(tacklers) - 1):
            edges.append((tacklers[i], tacklers[i + 1]))

# ======================
# 3️⃣ Buat adjacency list
# ======================
adj_list = {}
for src, dst in edges:
    adj_list.setdefault(src, []).append(dst)

# ======================
# 4️⃣ Buat adjacency matrix
# ======================
nodes = sorted(set([src for src, _ in edges] + [dst for _, dst in edges]))
adj_matrix = pd.DataFrame(0, index=nodes, columns=nodes, dtype=int)
for src, dst in edges:
    adj_matrix.loc[src, dst] = 1

# ======================
# 5️⃣ Print hasil adjacency list & matrix
# ======================
print("\n=== ADJACENCY LIST ===")
for node, targets in adj_list.items():
    print(f"{node} : {', '.join(targets)}")

print("\n=== ADJACENCY MATRIX ===")
print(adj_matrix.to_string())

# ======================
# 6️⃣ Analisis Dasar Graf
# ======================
print("\n=== ANALISIS DASAR GRAF ===")
total_nodes = len(nodes)
total_edges = len(edges)
print(f"Jumlah simpul (vertex): {total_nodes}")
print(f"Jumlah sisi (edge): {total_edges}")

# Hitung derajat keluar (out-degree)
out_degree = Counter([src for src, _ in edges])

# Top 5 pemain paling banyak mengoper bola / aksi keluar
top_active = out_degree.most_common(5)
print("\nPemain paling banyak mengoper bola / aksi keluar:")
for p, d in top_active:
    if p not in ["GOAL", "LOSS"]:
        print(f"  Pemain {p}: {d} kali")

# Node yang paling sering menembak ke GOAL
shooters = [src for src, dst in edges if dst == "GOAL"]
if shooters:
    print("\nPemain yang paling sering menembak ke GOAL:")
    for p, c in Counter(shooters).most_common():
        print(f"  Pemain {p}: {c} tembakan")

# Node yang paling sering kehilangan bola (ke LOSS)
losers = [src for src, dst in edges if dst == "LOSS"]
if losers:
    print("\nPemain yang paling sering kehilangan bola:")
    for p, c in Counter(losers).most_common():
        print(f"  Pemain {p}: {c} kali kehilangan bola")

print("\nAnalisis selesai ✅")
