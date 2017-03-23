import * as d3 from "d3";

export default function addLegend (svg) {
  const legendRectSize = 14;
  const legendSpacing = 4;
  const color = d3.scaleOrdinal()
    .domain(["red"])
    .range([0]);

  const legend = svg.selectAll(".legend")
    .data(color.domain())
    .enter()
    .append("g")
    .attr("transform", () => {
      const height = legendRectSize + legendSpacing;
      const offset =  height * color.domain().length / 2;
      const x = 2 * legendRectSize;
      const y = 1.1 * height - offset;
      return "translate(" + x + "," + y + ")";
    });

  legend.append("rect")
    .attr("width", legendRectSize)
    .attr("height", legendRectSize)
    .style("fill", (d) => d);

  legend.append("text")
    .attr("x", legendRectSize + legendSpacing)
    .attr("y", legendRectSize - legendSpacing + 2)
    .text("Possible outliers");
}
