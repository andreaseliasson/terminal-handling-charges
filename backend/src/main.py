from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Let's check for anomalies in terminal handling charges"

if __name__ == "__main__":
    app.run()
