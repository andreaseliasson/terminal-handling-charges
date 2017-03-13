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
    axios.get("http://127.0.0.1:5000/")
      .then(res => {
        const terminalHandlingCharges = res.data;
        this.setState({ terminalHandlingCharges });
      });
  }

  handleChange({name, value}) {
    this.setState({
     [name]: value
    });
  }

  handleSubmit(e) {
    e.preventDefault();
    // Make a post request to the API here
    const newCharge = {
      text: this.state.newCharge
    };
    this.setState((prevState) => ({
      newCharge: ""
    }));
  }

  render() {
    return (
      <div className={styles.app}>
        <h1>Anomaly Detection for terminal handling charges</h1>
        <KDEGraph countryCharges={this.state.terminalHandlingCharges}/>
        <Charge fields={Object.keys(this.state.newCharge)} onChange={this.handleChange.bind(this)}/>
      </div>
    );
  }
}

ReactDOM.render(<App/>, document.getElementById("app"));
