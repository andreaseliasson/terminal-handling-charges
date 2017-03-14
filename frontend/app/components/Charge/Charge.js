import React from "react";
import axios from "axios"
import ChargeForm from "./ChargeForm";
import styles from "./charge-form.css"

class Charge extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.baseUrl = "http://127.0.0.1:5000/";
    this.state = {
      "currency": "",
      "supplier_id": "",
      "port": "",
      "value": "",
      "outlier": ""
    };
  }

  handleChange({name, value}) {
    this.setState({
      [name]: value
    });
  }

  handleSubmit(e) {
    e.preventDefault();

    axios.post(this.baseUrl + 'charge', this.state)
      .then(response => {
        this.setState({outlier: response.data.outlier});
      })
      .catch(error => {
        console.log(error);
      });
  }

  render() {
    return (
      <div className="col-sm-offset-1 col-sm-4">
        <ChargeForm
          fields={Object.keys(this.state).filter(prop => prop !== "outlier")}
          outlier={this.state.outlier}
          onChange={this.handleChange.bind(this)}
          onSubmit={this.handleSubmit.bind(this)}
        />
      </div>
    );
  }
}

export default Charge