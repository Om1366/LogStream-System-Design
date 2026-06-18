from flask import Flask, request, jsonify
from database import save_log
from processor import process_log

app = Flask(__name__)


@app.route("/")
def home():
    return "LogStream API Running"


@app.route("/logs", methods=["POST"])
def ingest_log():

    log = request.json

    processed_log = process_log(log)

    save_log(processed_log)

    return jsonify({
        "status": "success",
        "message": "Log stored successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)