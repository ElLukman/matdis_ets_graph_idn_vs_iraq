from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# --- DATA LOADING ---
# Fungsi untuk memuat data statistik dari file JSON
def load_stats_data():
    with open('data/match_stat.json', 'r') as f:
        return json.load(f)

# Route untuk halaman utama, kita arahkan langsung ke possession
@app.route('/')
@app.route('/possession')
def possession_page():
    # Render file possession.html dan kirim variabel active_tab
    return render_template('possession.html', active_tab='possession')

# Route untuk halaman shooting
@app.route('/shooting')
def shooting_page():
    # Render file shooting.html dan kirim variabel active_tab
    return render_template('shooting.html', active_tab='shooting')

# Route untuk halaman tackle
@app.route('/tackle')
def tackle_page():
    # Render file tackle.html dan kirim variabel active_tab
    return render_template('tackle.html', active_tab='tackle')

# --- ROUTE API UNTUK DATA JSON ---
@app.route('/api/data/<stat_type>')
def get_stat_data(stat_type):
    stats_data = load_stats_data()
    # Ambil data sesuai tipe yang diminta (possession, shooting, atau tackle)
    if stat_type in stats_data:
        return jsonify(stats_data[stat_type])
    else:
        return jsonify({"error": "Data not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
