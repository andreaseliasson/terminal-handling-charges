import React from "react";
import styles from "./kde-graph.css"
import * as d3 from "d3";
import addLegend from "./legend"

class KDEGraph extends React.Component {
  constructor(props) {
    super(props);
  }

  draw_graph(country_charges) {
    const charge_values = country_charges.values;
    const charge_outliers = country_charges.outliers;

    const margin = {top: 40, right: 30, bottom: 50, left: 40};
    const width = 600 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;

    const x = d3.scaleLinear()
      .domain([d3.min(charge_values), d3.max(charge_values)])
      .range([0, width]);

    const y = d3.scaleLinear()
      .domain([0, 0.08])
      .range([height, 0]);

    const xAxis = d3.axisBottom(x);
    const yAxis = d3.axisLeft(y);

    const line = d3.line()
      .x((d) => x(d[0]))
      .y((d) => y(d[1]));

    const svg = d3.select(`.kde-container`).append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    svg.append("g")
      .attr("class", styles.x + styles.axis)
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

    svg.append("g")
      .attr("class", styles.y + styles.axis)
      .call(yAxis);

    svg.append("text")
      .attr("x", (width / 2))
      .attr("y", 0 - (margin.top / 2))
      .attr("text-anchor", "middle")
      .attr("class", styles.title)
      .text(`Distribution of Terminal Handling Charge Values for ${country_charges.country_code}`);

    svg.selectAll(".charge-value")
      .data(charge_values)
      .enter()
      .append("line")
      .style("stroke", "black")
      .attr("x1", (d) => x(d))
      .attr("y1", height - 10)
      .attr("x2", (d) => x(d))
      .attr("y2", height);

    svg.selectAll(".charge-outlier")
      .data(charge_outliers)
      .enter()
      .append("circle")
      .style("fill", "red")
      .attr("cx", (d) => x(d))
      .attr("cy", height - 15)
      .attr("r", 5);

    const kde = kernelDensityEstimator(epanechnikovKernel(5), x.ticks(100));

    svg.append("path")
      .datum(kde(charge_values))
      .attr("class", styles.line)
      .attr("d", line);

    addLegend(svg);

    function kernelDensityEstimator(kernel, x) {
      return (sample) => x.map((x) => [x, d3.mean(sample, (v) => kernel(x - v))]);
    }

    function epanechnikovKernel(scale) {
      return (u) => Math.abs(u /= scale) <= 1 ? .75 * (1 - u * u) / scale : 0;
    }
  }

  render() {
    return (
      <div className={"kde-container "  + "col-sm-7 " + styles.border}>
        <h4>Kernel Density Estimation Graphs</h4>
        {!this.props.countryCharges.length && <p>Crunching data...</p>}
        {this.props.countryCharges.map((country, i) => {
          return (
            <div key={i}>
              {this.draw_graph(country, i)}
            </div>
          )
        })}
      </div>
    );
  }
}

export default KDEGraph
