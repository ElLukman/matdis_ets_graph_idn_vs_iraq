from flask import Flask, render_template, jsonify, url_for
import os 

from passing import generate_possession_data
from shooting import  generate_shooting_data
from tackle_win import generate_tackle_data

app = Flask(__name__)

# Route untuk halaman utama, kita arahkan langsung ke possession
@app.route('/')
@app.route('/possession')
def possession_page():
    data_intervals = generate_possession_data()

    return render_template(
        'possession.html', 
        active_tab='possession',
        data_intervals=data_intervals
    )

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
    
# API Endpoint
@app.route('/api/data/<stat_type>')
def get_stat_data(stat_type):
    data = {}
    
    if stat_type == 'possession':
      
      data = generate_possession_data()
      for item in data: 
        if 'graph_image_url' in item: 
          item['graph_image_url'] = url_for('static', filename=item['graph_image_url'])
      return jsonify(data)
      
    elif stat_type == 'shooting':
      data = generate_shooting_data()
    elif stat_type == 'tackle':
      data = generate_tackle_data()
    else: 
      return jsonify({"error": "Data not found"})  
    
    if 'graph_image_url' in data: 
      data['graph_image_url'] = url_for('static', filename=data['graph_image_url'])
    
    return jsonify(data)

if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.dirname(__file__), 'data'), exist_ok=True)
    os.makedirs(os.path.join(os.path.dirname(__file__), 'static', 'img', 'passing_intervals'), exist_ok=True)
    app.run(debug=True)
