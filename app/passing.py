# passing_per_10min_show_with_legend.py
import pandas as pd
import networkx as nx

import matplotlib 
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
import math
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, 'data', 'matdis_sheet1.csv')
OUT_DIR = os.path.join(SCRIPT_DIR, 'static', 'img', 'passing_intervals')

os.makedirs(OUT_DIR, exist_ok=True)

def draw_pitch(ax):
    """Menggambar lapangan sepak bola sederhana"""
    ax.add_patch(Rectangle((0, 0), 200, 130, fill=False, color='green', lw=2))
    ax.plot([100, 100], [0, 130], color='green', lw=2)
    ax.add_patch(Rectangle((-2, 55), 2, 20, fill=False, color='green', lw=2))
    ax.add_patch(Rectangle((200, 55), 2, 20, fill=False, color='green', lw=2))
    ax.set_xlim(-10, 210)
    ax.set_ylim(-10, 140)
    ax.set_aspect('equal')
    ax.axis('off')

def build_graph_from_df(df_segment, pass_col_name='pass'):
    """Membangun graph passing dari dataframe per interval"""
    G = nx.DiGraph()
    for _, row in df_segment.iterrows():
        val = row.get(pass_col_name, None)
        if pd.isna(val):
            continue
        s = str(val).replace('.', ',').replace(' ', '')
        passes = [p for p in s.split(',') if p]
        for i in range(len(passes) - 1):
            passer = passes[i].strip()
            receiver = passes[i + 1].strip()
            if passer and receiver:
                if G.has_edge(passer, receiver):
                    G[passer][receiver]['weight'] += 1
                else:
                    G.add_edge(passer, receiver, weight=1)
    return G

def analyze_and_plot(G, pos, interval_name, previous_nodes, out_dir=OUT_DIR, show_plot=False):
    """Analisis dan plot jaringan passing"""
    degree_centrality = nx.degree_centrality(G)
    in_strength = dict(G.in_degree(weight='weight'))
    out_strength = dict(G.out_degree(weight='weight'))
    df_cent = pd.DataFrame({
        'In': pd.Series(in_strength),
        'Out': pd.Series(out_strength),
        'DegreeCentrality': pd.Series(degree_centrality)
    }).fillna(0)
    df_cent['Total'] = df_cent['In'] + df_cent['Out']
    df_cent = df_cent.sort_values('Total', ascending=False)

    # print(f"\n=== Interval {interval_name} ===")
    # print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
    
    top_players_list = []
    
    if not df_cent.empty:
        # print("Top pemain (by Total):")
        # print(df_cent.head(5))
        
        for index, row in df_cent.head(5).iterrows():
            top_players_list.append({
                "name": f"Pemain #{index}",
                "stat": int(row['Total'])
            })

    fig = plt.figure(figsize=(12, 7))
    ax = plt.gca()
    ax.set_facecolor('black')
    fig.set_facecolor('black')
    
    draw_pitch(ax)

    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges] if edges else []
    max_w = max(weights) if weights else 1
    scaled_weights = [5 * (w / max_w) for w in weights]

    node_sizes = [3000 * degree_centrality.get(n, 0.05) for n in G.nodes()]

    # Pemain baru → kuning, lama → biru
    node_colors = []
    new_players_str = []
    for n in G.nodes():
        if n not in previous_nodes:
            node_colors.append('yellow')
            new_players_str.append(str(n))
        else:
            node_colors.append('skyblue')

    # Gambar network
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.95)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray', width=scaled_weights, arrows=True, arrowsize=18)
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)

    plt.title(f"Passing Network — {interval_name}", fontsize=14, color='white')
    
    # Tambahkan legend untuk pemain baru/lama
    legend_elements = [
        Patch(facecolor='skyblue', edgecolor='black', label='Pemain Lama'),
        Patch(facecolor='yellow', edgecolor='black', label='Pemain Baru')
    ]
    legend = ax.legend(handles=legend_elements, loc='upper right', fontsize=9)
    plt.setp(legend.get_texts(), color='black')

    plt.tight_layout()
    
    img_filename = f"passing_interval_{interval_name.replace(' ', '_')}.png"
    img_path_abs = os.path.join(OUT_DIR, img_filename)
    img_path_relative = f"img/passing_intervals/{img_filename}"
    
    plt.savefig(img_path_abs, dpi=150, facecolor='black', bbox_inches='tight')
    print(f"Gambar disimpan: {img_path_abs}")
    plt.close(fig)
    
    if new_players_str:
        pass
        # print(f"Pemain baru di interval {interval_name}: {', '.join(new_players_str)}")

    return {
        "interval_name": interval_name,
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "top_players": top_players_list,
        "new_players": ", ".join(new_players_str) if new_players_str else "Tidak ada",
        "graph_image_url": img_path_relative 
    }

def generate_possession_data():
    # Error Handling
    if not os.path.exists(CSV_PATH):
        print (f"Error Tidak ditemukan {CSV_PATH}")
        return []
    
    df = pd.read_csv(CSV_PATH)
    df.columns = [c.lower() for c in df.columns]

    if 'menit' not in df.columns:
        raise ValueError("CSV tidak memiliki kolom 'menit'.")
        return []
    
    pass_col = 'pass' if 'pass' in df.columns else None
    if not pass_col:
        candidates = [c for c in df.columns if 'pass' in c or 'umpan' in c]
        if candidates:
            pass_col = candidates[0]
        else:
            raise ValueError("Tidak menemukan kolom 'pass' atau sejenisnya di CSV.")

    df['menit'] = pd.to_numeric(df['menit'], errors='coerce')
    df = df.dropna(subset=['menit'])
    df['menit'] = df['menit'].astype(int)

    max_min = int(df['menit'].max())
    n_intervals = math.ceil((max_min + 1) / 10)

    base_pos = {
        '1': (0, 65), '21': (50, 110), '3': (50, 85), '5': (50, 55),
        '2': (50, 30), '17': (100, 95), '14': (100, 50), '15': (140, 110),
        '19': (140, 70), '23': (140, 35), '13': (190, 65),
        
        '10': (190, 65), '11': (140, 110), '9': (140, 35), '7': (100, 50),
        '22': (50, 110),
    }

    previous_nodes = set()
    all_interval_data = []

    for i in range(n_intervals):
        start = i*10
        end = start + 9
        seg = df[(df['menit'] >= start) & (df['menit'] <= end)]
        interval_name = f"{start}-{end}"
        if seg.empty:
            # print(f"Interval {interval_name} kosong — dilewati.")
            continue

        G = build_graph_from_df(seg, pass_col_name=pass_col)
        if G.number_of_nodes() == 0:
            continue

        spring = nx.spring_layout(G, seed=42)
        pos = {node: base_pos.get(str(node), spring[node]) for node in G.nodes()}
        
        interval_data = analyze_and_plot(G, pos, interval_name, previous_nodes)
        all_interval_data.append(interval_data)
        
        previous_nodes.update(G.nodes())
        
    return all_interval_data
