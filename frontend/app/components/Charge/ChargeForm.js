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
    return (
      <div className="charge">
        <form onSubmit={this.onSubmit.bind(this)} className={styles.chargeForm}>
          {this.props.fields.map((field, i) => {
            return (
              <div key={i}>
                <label>
                  {field}
                  <input
                    className={styles.formInput}
                    type="text"
                    name={field}
                    value={this.props.fields[field]}
                    onChange={this.onFieldChange.bind(this)}/>
                </label>
              </div>
            )
          })}
          <input className={styles.btn} type="submit" value="Submit new Charge"/>
          {/* Slightly obscure predicate but reason is outlier takes on values 0 and 1 */}
          {this.props.outlier !== ""  &&
            <p>Status: {this.props.outlier ?
              (<b className={styles.red}>Outlier</b>)
              : (<b className={styles.green}>OK</b>)}</p>
          }
        </form>
      </div>
    );
  }
}

export default ChargeForm