// static/js/match_stats.js (Versi Final dengan D3.js)

/**
 * Fungsi ini menerima container HTML dan data grafik dari Python,
 * lalu menggambarnya menggunakan D3.js.
 * @param {HTMLElement} container - Elemen div 'graph-container'.
 * @param {object} graphData - Objek berisi 'nodes' dan 'links'.
 */
function drawPossessionGraph(container, graphData) {
  const width = container.offsetWidth;
  const height = container.offsetHeight;

  const svg = d3.select(container)
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", [-width / 2, -height / 2, width, height]);

  const nodes = graphData.nodes.map(d => Object.create(d));
  const links = graphData.links.map(d => Object.create(d));

  const simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d => d.id).distance(100))
    .force("charge", d3.forceManyBody().strength(-150))
    .force("center", d3.forceCenter());

  const link = svg.append("g")
    .attr("stroke", "#999")
    .attr("stroke-opacity", 0.6)
    .selectAll("line")
    .data(links)
    .join("line")
    .attr("stroke-width", d => Math.sqrt(d.value)); // Lebar garis berdasarkan 'value'

  const node = svg.append("g")
    .attr("stroke", "#fff")
    .attr("stroke-width", 1.5)
    .selectAll("circle")
    .data(nodes)
    .join("circle")
    .attr("r", 8) // Radius lingkaran
    .attr("fill", "#22c55e"); // Warna hijau

  const label = svg.append("g")
    .attr("class", "labels")
    .selectAll("text")
    .data(nodes)
    .enter().append("text")
    .attr("dx", 12)
    .attr("dy", ".35em")
    .style("fill", "#fff")
    .style("font-size", "12px")
    .text(d => d.id);

  node.call(d3.drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended));

  simulation.on("tick", () => {
    link
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y);

    node
      .attr("cx", d => d.x)
      .attr("cy", d => d.y);

    label
      .attr("x", d => d.x)
      .attr("y", d => d.y);
  });

  // Fungsi-fungsi untuk drag
  function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
  }

  function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }
}