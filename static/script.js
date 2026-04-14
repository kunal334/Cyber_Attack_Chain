document.addEventListener("DOMContentLoaded", function() {

    const graph = JSON.parse(graphData);

    const svg = d3.select("svg");
    const width = 600,
        height = 400;

    const simulation = d3.forceSimulation(graph.nodes)
        .force("link", d3.forceLink(graph.links).distance(100).id(d => d.id))
        .force("charge", d3.forceManyBody().strength(-300))
        .force("center", d3.forceCenter(width / 2, height / 2));

    const link = svg.selectAll("line")
        .data(graph.links)
        .enter().append("line")
        .attr("stroke", "#00ffcc")
        .attr("stroke-width", 2);

    const node = svg.selectAll("circle")
        .data(graph.nodes)
        .enter().append("circle")
        .attr("r", 10)
        .attr("fill", d => d.id.includes("192") ? "red" : "cyan");

    const text = svg.selectAll("text")
        .data(graph.nodes)
        .enter().append("text")
        .text(d => d.id)
        .attr("font-size", 12)
        .attr("fill", "white");

    node.append("title")
        .text(d => d.id);

    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        text
            .attr("x", d => d.x + 12)
            .attr("y", d => d.y);
    });

    console.log(graph);
});