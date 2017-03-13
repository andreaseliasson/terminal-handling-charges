import React from "react";
import axios from "axios"
import ChargeForm from "./ChargeForm";

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
      "value": ""
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
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      });
  }

  render() {
    return (
      <div>
        <ChargeForm
          fields={Object.keys(this.state)}
          onChange={this.handleChange.bind(this)}
          onSubmit={this.handleSubmit.bind(this)}
        />
      </div>
    );
  }
}

export default Charge