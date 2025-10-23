document.addEventListener("DOMContentLoaded", () => {
  const tabs = ["possession", "shooting", "tackle"];
  
  tabs.forEach(tab => {
    document.getElementById(`tab-${tab}`).addEventListener("click", () => {
      loadTab(tab);
    });
  });
});

// Fungsi utama untuk memuat data tab
function loadTab(tab) {
  fetch(`/api/data/${tab}`)
    .then(res => res.json())
    .then(data => {
      // Panggil fungsi untuk merender info panel dan player list
      renderInfoPanel(tab, data);
      renderPlayerList(data);
      // Panggil fungsi untuk merender graph (dari tahap selanjutnya)
      renderGraph(tab, data);
    });
}

// Fungsi untuk merender info panel sesuai UI
function renderInfoPanel(tab, data) {
  const infoPanel = document.getElementById("info-panel");
  let htmlContent = '';

  if (tab === 'possession') {
    htmlContent = `
      <h2 class="text-xl font-semibold text-green-400">Possession Ball:</h2>
      <div class="w-24 h-24 mx-auto border-4 border-neutral-700 rounded-full flex items-center justify-center">
          <p class="text-3xl font-bold">${data.summary.percentage}%</p>
      </div>
      <p><b>Completed:</b> ${data.summary.completed}</p>
      <p><b>Intercepted:</b> ${data.summary.intercepted}</p>
      <p><b>Total Passes:</b> ${data.summary.total_passes}</p>
      <p><b>xPass:</b> ${data.summary.xPass}</p>
    `;
  } else if (tab === 'shooting') {
    htmlContent = `
    
      <h2 class="text-xl font-semibold text-green-400 mt-4 mb-4">Total Shoot:</h2>
        <div class="w-32 h-32 rounded-full border-8 mb-6 border-white flex items-center justify-center">
          <p class="text-3xl font-bold">${data.summary.total_shots}</p>
        </div>
      <p><b>Shot on Target:</b> ${data.summary.on_target}</p>
      <p><b>Shot off Target:</b> ${data.summary.off_target}</p>
      <p><b>xGoal:</b> ${data.summary.xGoal}</p>
    `;
  } else if (tab === 'tackle') {
    htmlContent = `
      <h2 class="text-xl font-semibold text-green-400 mb-2">Total Tackle Won:</h2>
      <div class="w-24 h-24 mx-auto border-4 border-neutral-700 rounded-full flex items-center justify-center">
          <p class="text-3xl font-bold">${data.summary.total_tackles}</p>
      </div>
      <p><b>Most Tackle Player:</b> ${data.summary.most_tackles_player}</p>
    `;
  }
  infoPanel.innerHTML = htmlContent;
}

// Fungsi untuk merender daftar pemain
function renderPlayerList(data) {
    const playerContainer = document.getElementById("player-list-container");
    let playerItems = data.players.map(player => `<li>${player.name} (${player.stat})</li>`).join('');

    playerContainer.innerHTML = `
        <h3 class="text-green-400 font-semibold mb-2">Player:</h3>
        <ol class="list-decimal list-inside space-y-1">
            ${playerItems}
        </ol>
    `;
}

// Fungsi render graph 
function renderGraph(tab, data) {
  const container = document.getElementById("graph-container");
  
  // Cek apakah API mengirimkan graph_image_url
  if (data.graph_image_url) {
    // Jika ya, buat tag <img>
    // 'data.graph_image_url' sudah berisi path /static/img/namafile.png dari app.py
    container.innerHTML = `
      <img 
        src="${data.graph_image_url}" 
        alt="Grafik ${tab}" 
        class="max-w-full max-h-full object-contain"
      >
    `;
  } else {
    // Jika tidak ada URL gambar, tampilkan pesan error
    container.innerHTML = "Grafik tidak dapat dimuat.";
  }
}