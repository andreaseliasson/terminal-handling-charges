from flask import Flask
app = Flask(__name__)


@app.route("/")
def start():
    return "Let's check for anomalies in terminal handling charges"


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST')
    return response

if __name__ == "__main__":
    app.run()
