import React from "react";
import ReactDOM from "react-dom";
import axios from "axios"

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      terminalHandlingCharges: []
    };
  }

  componentDidMount() {
    axios.get("http://127.0.0.1:5000/")
      .then(res => {
        const terminalHandlingCharges = res.data;
        this.setState({ terminalHandlingCharges });
      });
  }

  render() {
    return <h1>Anomaly Detection for terminal handling charges</h1>
  }
}

ReactDOM.render(<App/>, document.getElementById("app"));
