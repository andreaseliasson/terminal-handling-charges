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
      <div className={styles.border}>
        <h4>Submit new Charge</h4>
        <form onSubmit={this.onSubmit.bind(this)} className="form-horizontal">
          {this.props.fields.map((field, i) => {
            return (
              <div key={i} className="form-group">
                <label className="col-sm-2 control-label">
                  {field}
                </label>
                <div className="col-sm-offset-1 col-sm-9">
                  <input
                    type="text"
                    name={field}
                    className="form-control"
                    value={this.props.fields[field]}
                    onChange={this.onFieldChange.bind(this)}/>
                </div>
              </div>
            )
          })}
          <input className="btn btn-primary" type="submit" value="Submit new Charge" />
        </form>
        {/* Slightly obscure predicate but reason is outlier takes on values 0 and 1 */}
        {this.props.outlier !== ""  &&
          <p>Status: {this.props.outlier ?
            (<b className={styles.red}>Outlier</b>)
            : (<b className={styles.green}>OK</b>)}</p>
        }
      </div>
    );
  }
}

export default ChargeForm