import React from "react";
import ReactDOM from "react-dom";
import axios from "axios"
import KDEGraph from "../KDEGraph/KDEGraph";
import styles from './app.css';
import Charge from "../Charge/Charge";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.baseUrl = "http://127.0.0.1:5000/";
    this.state = {
      terminalHandlingCharges: [],
      newCharge: {
        "currency": "",
        "supplier_id": "",
        "port": "",
        "value": ""
      }
    };
  }

  componentDidMount() {
    axios.get(this.baseUrl)
      .then(res => {
        const terminalHandlingCharges = res.data;
        this.setState({ terminalHandlingCharges });
      });
  }

  handleChange({name, value}) {
    // This could be solved more elegantly with _.extend to limit immutability
    let newState = this.state.newCharge;
    newState[name] = value;
    this.setState({newCharge: newState});
  }

  handleSubmit(e) {
    e.preventDefault();

    axios.post(this.baseUrl + 'charge', this.state.newCharge)
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      });
  }

  render() {
    return (
      <div className={styles.app}>
        <h1>Anomaly Detection for terminal handling charges</h1>
        <KDEGraph countryCharges={this.state.terminalHandlingCharges}/>
        <Charge
          fields={Object.keys(this.state.newCharge)}
          onChange={this.handleChange.bind(this)}
          onSubmit={this.handleSubmit.bind(this)}
        />
      </div>
    );
  }
}

ReactDOM.render(<App/>, document.getElementById("app"));
