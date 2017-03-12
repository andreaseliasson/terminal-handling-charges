import React from "react";
import styles from "./kde-graph.css"
import * as d3 from "d3";

class KDEGraph extends React.Component {
  constructor(props) {
    super(props);
  }

  render_graph(country_charges) {
    const charge_values = country_charges.values;
    const charge_outliers = country_charges.outliers;


    const margin = {top: 20, right: 30, bottom: 30, left: 40};
    const width = 600 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;

    const x = d3.scaleLinear()
      .domain([d3.min(charge_values), d3.max(charge_values)])
      .range([0, width]);

    const y = d3.scaleLinear()
      .domain([0, .1])
      .range([height, 0]);

    const xAxis = d3.axisBottom(x);
    const yAxis = d3.axisLeft(y);

    const line = d3.line()
      .x(function(d) { return x(d[0]); })
      .y(function(d) { return y(d[1]); });

    const svg = d3.select(".kde-container").append("svg")
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

    svg.selectAll(".charge-value")
      .data(charge_values)
      .enter()
      .append("line")
      .style("stroke", "black")
      .attr("x1", function(d) { return x(d)})
      .attr("y1", height - 10)
      .attr("x2", function(d) { return x(d)})
      .attr("y2", height);

    svg.selectAll(".charge-outlier")
      .data(charge_outliers)
      .enter()
      .append("circle")
      .style("fill", "red")
      .attr("cx", function(d) { return x(d) })
      .attr("cy", height - 15)
      .attr("r", 5);

    const kde = kernelDensityEstimator(epanechnikovKernel(5), x.ticks(100));

    svg.append("path")
      .datum(kde(charge_values))
      .attr("class", styles.line)
      .attr("d", line);

    function kernelDensityEstimator(kernel, x) {
      return function(sample) {
        return x.map(function(x) {
          return [x, d3.mean(sample, function(v) { return kernel(x - v); })];
        });
      };
    }

    function epanechnikovKernel(scale) {
      return function(u) {
        return Math.abs(u /= scale) <= 1 ? .75 * (1 - u * u) / scale : 0;
      };
    }

  }

  render() {
    return (
      <div className="kde-container">
        <h2>Kernel Density Estimation Graphs</h2>
        {this.props.countryCharges.map((country, i) => {
          return (
            <div key={i}>
              {this.render_graph(country)}
            </div>
          )
        })}
      </div>
    );
  }
}

export default KDEGraph
