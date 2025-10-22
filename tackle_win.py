import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Data Tackle
tackle_data = {
    '5': 1, '2': 1, '21': 4, '15': 5, '17': 6, '14': 3, '3': 4,
    '10': 2, '19': 2, '1': 1, '22': 6, '8': 1, '11': 1
}

subs_players = ['10', '22', '8', '11']

# Layout formasi pemain
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
    'Gawang': (200, 65),
    '10': (220, 100),
    '22': (220, 80),
    '8': (220, 60),
    '11': (220, 40)
}

# Gambar lapangan
def draw_pitch(ax):
    ax.add_patch(Rectangle((0, 0), 200, 130, fill=False, color='green', lw=2))
    ax.plot([100, 100], [0, 130], color='green', lw=2)
    ax.add_patch(Rectangle((-2, 55), 2, 20, fill=False, color='green', lw=2))
    ax.add_patch(Rectangle((200, 55), 2, 20, fill=False, color='green', lw=2))
    ax.set_xlim(-10, 240)
    ax.set_ylim(-10, 140)
    ax.set_aspect('equal')
    ax.axis('off')

G = nx.Graph()

for p in pos.keys():
    G.add_node(p, tackle=tackle_data.get(p, 0))

# Visualisasi tackle
plt.figure(figsize=(16, 9))
ax = plt.gca()
draw_pitch(ax)

node_colors = [
    'lightgrey' if node in subs_players else 'skyblue'
    for node in G.nodes()
]

# Ukuran node sesuai jumlah tackle
node_sizes = [700 + (G.nodes[n]['tackle'] * 150) for n in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.95)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Label jumlah tackle
for node, (x, y) in pos.items():
    tackle_count = G.nodes[node]['tackle']
    if tackle_count > 0:
        ax.text(x, y + 4, f"{tackle_count}x", ha='center', fontsize=9, color='black')

plt.title("Visualisasi Tackle Win Pemain (Dengan Substitusi)", fontsize=17)
plt.tight_layout()
plt.show()