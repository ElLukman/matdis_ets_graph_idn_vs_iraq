import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Data shooting
shooting_data = {
    '17': 2, '19': 1, '13': 2, '23': 1, '21': 1, '2': 1
}

# Data tackle
tackle_data = {
    '5': 1, '2': 1, '21': 4, '15': 5, '17': 6, '14': 3, '3': 4,
    '10': 2, '19': 2, '1': 1, '22': 6, '8': 1, '11': 1
}

# Player yang substitusi
subs_players = ['10', '22', '8', '11']

# Layout posisi pemain
pos = {
    '1': (0, 65),
    '21': (30, 110),
    '3': (30, 85),
    '5': (30, 55),
    '2': (30, 30),
    '17': (70, 95),
    '14': (70, 50),
    '15': (110, 110),
    '19': (110, 70),
    '23': (110, 35),
    '13': (150, 65),
    'Gawang': (200, 65)
}

pos_subs = {
    '10': (220, 100),
    '22': (220, 80),
    '8':  (220, 60),
    '11': (220, 40)
}

# Gabungkan posisi untuk tackle (biar subs ikut)
pos_tackle = pos.copy()
pos_tackle.update(pos_subs)

# Fungsi buat lapangan
def draw_pitch(ax):
    ax.add_patch(Rectangle((0, 0), 200, 130, fill=False, color='green', lw=2))
    ax.plot([100, 100], [0, 130], color='green', lw=2)
    ax.add_patch(Rectangle((-2, 55), 2, 20, fill=False, color='green', lw=2))
    ax.add_patch(Rectangle((200, 55), 2, 20, fill=False, color='green', lw=2))
    ax.set_xlim(-10, 240)
    ax.set_ylim(-10, 140)
    ax.set_aspect('equal')
    ax.axis('off')

# Visualisasi shooting
G_shoot = nx.DiGraph()

# Tambahkan semua pemain utama
main_players = [p for p in pos.keys() if p != 'Gawang']
G_shoot.add_nodes_from(main_players + ['Gawang'])

# edge shooting
for player, total in shooting_data.items():
    if player in G_shoot.nodes():
        G_shoot.add_edge(player, 'Gawang', weight=total)

# Gambar lapangan
plt.figure(figsize=(16, 9))
ax = plt.gca()
draw_pitch(ax)

node_colors = []
for node in G_shoot.nodes():
    if node == 'Gawang':
        node_colors.append('tomato')
    elif node in shooting_data:
        node_colors.append('lightgreen')
    else:
        node_colors.append('skyblue')

edges = G_shoot.edges()
weights = [G_shoot[u][v]['weight'] for u, v in edges]
max_weight = max(weights) if weights else 1
scaled_weights = [3 * (w / max_weight) for w in weights]

nx.draw_networkx_nodes(G_shoot, pos, node_color=node_colors, node_size=1000, alpha=0.95)
nx.draw_networkx_edges(
    G_shoot, pos, edgelist=edges, edge_color='red', style='dashed',
    width=scaled_weights, arrows=True, arrowsize=20
)
nx.draw_networkx_labels(G_shoot, pos, font_size=10, font_weight='bold')

edge_labels = nx.get_edge_attributes(G_shoot, 'weight')
nx.draw_networkx_edge_labels(G_shoot, pos, edge_labels=edge_labels, font_color='blue', font_size=8)

plt.title("Visualisasi Shooting Pemain", fontsize=17)
plt.tight_layout()
plt.show()

# Visualisasi tackle
G_tackle = nx.Graph()

# Tambahkan semua pemain
for p in pos_tackle.keys():
    G_tackle.add_node(p, tackle=tackle_data.get(p, 0))  # kalau ga ada di data, tackle = 0

plt.figure(figsize=(16, 9))
ax = plt.gca()
draw_pitch(ax)

node_colors_tackle = [
    'lightgrey' if node in subs_players else 'skyblue'
    for node in G_tackle.nodes()
]

node_sizes = [700 + (G_tackle.nodes[n]['tackle'] * 150) for n in G_tackle.nodes()]

nx.draw_networkx_nodes(G_tackle, pos_tackle, node_color=node_colors_tackle, node_size=node_sizes, alpha=0.95)
nx.draw_networkx_labels(G_tackle, pos_tackle, font_size=10, font_weight='bold')

for node, (x, y) in pos_tackle.items():
    tackle_count = G_tackle.nodes[node]['tackle']
    if tackle_count > 0:
        ax.text(x, y + 4, f"{tackle_count}x", ha='center', fontsize=9, color='black')

plt.title("Visualisasi Tackle Pemain", fontsize=17)
plt.tight_layout()
plt.show()