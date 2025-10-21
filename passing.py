import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# --- LANGKAH 1: MEMUAT DATA ---
df = pd.read_csv('Matdis-Indonesia-Iraq - Sheet1.csv')
G = nx.DiGraph()

# --- LANGKAH 2: MEMBANGUN GRAF PASSING ---
for index, row in df.iterrows():
    if pd.notna(row['Pass']):
        passes = str(row['Pass']).replace('.', ',').replace(' ', '').split(',')
        passes = [p for p in passes if p]
        for i in range(len(passes) - 1):
            passer = passes[i].strip()
            receiver = passes[i + 1].strip()
            if passer and receiver:
                if G.has_edge(passer, receiver):
                    G[passer][receiver]['weight'] += 1
                else:
                    G.add_edge(passer, receiver, weight=1)

print("Graf berhasil dibuat!")
print(f"Jumlah pemain (node): {G.number_of_nodes()}")
print(f"Jumlah interaksi umpan (edge): {G.number_of_edges()}")

# --- LANGKAH 3: POSISI PEMAIN (FORMASI) ---
pos = {
    '1': (0, 65),
    '21': (50, 110),
    '3': (50, 85),
    '5': (50, 55),
    '2': (50, 30),
    '17': (100, 95),
    '14': (100, 50),
    '15': (140, 110),
    '19': (140, 70),
    '23': (140, 35),
    '13': (190, 65),
}

# Tambahkan posisi acak untuk pemain yang tidak ada di formasi
pos_random = nx.spring_layout(G)
for node in G.nodes():
    if node not in pos:
        print(f"PERINGATAN: Pemain '{node}' tidak ada di formasi. Diberi posisi acak.")
        pos[node] = pos_random[node]

# --- LANGKAH 4: FUNGSI LAPANGAN ---
def draw_pitch(ax):
    ax.add_patch(Rectangle((0, 0), 200, 130, fill=False, color='green', lw=2))
    ax.plot([100, 100], [0, 130], color='green', lw=2)
    ax.add_patch(Rectangle((-2, 55), 2, 20, fill=False, color='green', lw=2))
    ax.add_patch(Rectangle((200, 55), 2, 20, fill=False, color='green', lw=2))
    ax.set_xlim(-10, 210)
    ax.set_ylim(-10, 140)
    ax.set_aspect('equal')
    ax.axis('off')

# --- LANGKAH 5: ANALISIS STATISTIK PEMAIN ---
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G, weight='weight')
in_strength = G.in_degree(weight='weight')
out_strength = G.out_degree(weight='weight')

df_centrality = pd.DataFrame({
    'In (Terima Umpan)': dict(in_strength),
    'Out (Umpan Keluar)': dict(out_strength),
    'Degree Centrality': degree_centrality,
    'Betweenness': betweenness_centrality
}).fillna(0)

df_centrality['Total Aktivitas Umpan'] = df_centrality['In (Terima Umpan)'] + df_centrality['Out (Umpan Keluar)']
df_centrality = df_centrality.sort_values(by='Total Aktivitas Umpan', ascending=False)

print("\n=== ANALISIS PEMAIN PALING BERPENGARUH ===")
print(df_centrality.round(3))
print("\nPemain paling berpengaruh berdasarkan aktivitas passing:")
print(df_centrality.head(3))

# --- LANGKAH 6: ANALISIS SINERGI ANTAR PEMAIN ---
synergy_list = []
for u, v, data in G.edges(data=True):
    if G.has_edge(v, u):  # cek umpan dua arah
        total = data['weight'] + G[v][u]['weight']
        synergy_list.append(((u, v), total))

if synergy_list:
    synergy_sorted = sorted(synergy_list, key=lambda x: x[1], reverse=True)
    print("\n=== ANALISIS SINERGI PEMAIN (UMPAN TIMBAL BALIK) ===")
    for (p1, p2), total in synergy_sorted[:5]:
        print(f"{p1} ↔ {p2}: {total} kali saling umpan")
else:
    print("\nTidak ada pasangan pemain yang saling melakukan umpan dua arah.")

# --- LANGKAH 7: VISUALISASI JARINGAN PASSING DI LAPANGAN ---
plt.figure(figsize=(16, 9))
ax = plt.gca()
draw_pitch(ax)

edges = G.edges()
weights = [G[u][v]['weight'] for u, v in edges]
max_weight = max(weights) if weights else 1
scaled_weights = [5 * (w / max_weight) for w in weights]

node_sizes = [3000 * degree_centrality.get(n, 0.1) for n in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=node_sizes, alpha=0.9)
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray', width=scaled_weights, arrows=True, arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)

plt.title("Visualisasi Jaringan Passing Pemain (Dengan Lapangan dan Analisis)", fontsize=18)
plt.tight_layout()
plt.show()

# --- LANGKAH 8: VISUALISASI BAR CHART PEMAIN PALING AKTIF ---
top_players = df_centrality.head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_players.index, top_players['Total Aktivitas Umpan'], color='skyblue')
plt.gca().invert_yaxis()
plt.title("Top 10 Pemain Paling Aktif dalam Passing", fontsize=16)
plt.xlabel("Total Aktivitas Umpan (In + Out)")
plt.ylabel("Nomor Pemain")
plt.tight_layout()
plt.show()
