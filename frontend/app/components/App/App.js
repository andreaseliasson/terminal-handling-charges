import React from "react";
import ReactDOM from "react-dom";
import axios from "axios"
import KDEGraph from "../KDEGraph/KDEGraph";
import styles from './app.css';
import Charge from "../Charge/Charge";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.baseUrl = "http://127.0.0.1:5000/";
    this.state = {
      terminalHandlingCharges: []
    };
  }

  componentDidMount() {
    axios.get(this.baseUrl)
      .then(res => {
        const terminalHandlingCharges = res.data;
        this.setState({ terminalHandlingCharges });
      });
  }

  render() {
    return (
      <div className="container">
        <h1>Outlier Detection for Terminal Handling Charges</h1>
        <div className="row">
          <KDEGraph countryCharges={this.state.terminalHandlingCharges}/>
          <Charge/>
        </div>
      </div>
    );
  }
}

ReactDOM.render(<App/>, document.getElementById("app"));
