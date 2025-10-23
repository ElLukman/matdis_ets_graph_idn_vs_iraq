import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os 

def generate_shooting_data():
    
    output_dir = 'static/img'
    os.makedirs(output_dir, exist_ok=True)
    graph_filename = 'shooting_graph.png'
    graph_filepath = os.path.join(output_dir, graph_filename)
    
    # Data shooting
    shooting_data = {
        '17': 2, '19': 1, '13': 2, '23': 1, '21': 1, '2': 1
    }
    
    total_shots = sum(shooting_data.values()) 
    summary_data = { 
        "total_shots": total_shots, 
        "on_target": 1, 
        "off_target": 7, 
        "xGoal": 0.31 
    }
    
    # Data pemain (top 5 shooter dari data di atas)
    top_shooters = sorted(shooting_data.items(), key=lambda item: item[1], reverse=True)[:5]
    player_list = [
        {"name": f"No Punggung #{p}", "stat": s} for p, s in top_shooters
    ]

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
        'Gawang': (200, 65)
    }

    # Gambar lapang
    def draw_pitch(ax):
        ax.add_patch(Rectangle((0, 0), 200, 130, fill=False, color='green', lw=2))
        ax.plot([100, 100], [0, 130], color='green', lw=2)
        ax.add_patch(Rectangle((-2, 55), 2, 20, fill=False, color='green', lw=2))
        ax.add_patch(Rectangle((200, 55), 2, 20, fill=False, color='green', lw=2))
        ax.set_xlim(-10, 240)
        ax.set_ylim(-10, 140)
        ax.set_aspect('equal')
        ax.axis('off')

    G = nx.DiGraph()
    G.add_nodes_from(pos.keys())

    for player, total in shooting_data.items():
        if player in G.nodes():
            G.add_edge(player, 'Gawang', weight=total)

    # Visualisasi
    plt.figure(figsize=(16, 9))
    ax = plt.gca()
    draw_pitch(ax)

    node_colors = []
    for node in G.nodes():
        if node == 'Gawang':
            node_colors.append('tomato')
        elif node in shooting_data:
            node_colors.append('lightgreen')
        else:
            node_colors.append('skyblue')

    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]
    max_weight = max(weights) if weights else 1
    scaled_weights = [3 * (w / max_weight) for w in weights]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1500, alpha=0.95)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', style='dashed',
                        width=scaled_weights, arrows=True, arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue', font_size=8)

    plt.title("Visualisasi Shooting Pemain (Tanpa Substitusi)", fontsize=17)
    plt.tight_layout()
    plt.savefig(graph_filepath)
    plt.close()

    return { 
        "summary": summary_data,
        "players":player_list, 
        "graph_image_url": f"img/{graph_filename}"
    }