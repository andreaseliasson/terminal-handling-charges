import React from "react";
import styles from "./charge-form.css"

class ChargeForm extends React.Component {
  constructor(props) {
    super(props);
  }

  onFieldChange(e) {
    this.props.onChange(e.target);
  }

  onSubmit(e) {
    this.props.onSubmit(e);
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
        {this.props.outlier &&
          <p>Status: {this.props.outlier ?
            (<b className={styles.red}>Outlier</b>)
            : (<b className={styles.green}>OK</b>)}</p>
        }
      </div>
    );
  }
}

export default ChargeForm