import React from "react";

class Charge extends React.Component {
  constructor(props) {
    super(props);
  }

  onFieldChange(e) {
    this.props.onChange(e.target);
  }

  onSubmit(e) {
    this.props.onSubmit(e)
  }

  render() {
    console.log(this.props.fields);
    return (
      <div className="charge">
        <form onSubmit={this.onSubmit.bind(this)}>
          {this.props.fields.map((field, i) => {
            return (
              <div key={i}>
                <label>
                  {field}
                  <input
                    type="text"
                    name={field}
                    value={this.props.fields[field]}
                    onChange={this.onFieldChange.bind(this)}/>
                </label>
              </div>
            )
          })}
          <input type="submit" value="Submit"/>
        </form>
      </div>
    );
  }
}

export default Charge