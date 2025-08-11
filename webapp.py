from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/packets")
def get_packets():
    file_path = os.path.join("captures", "packets.json")
    if os.path.exists(file_path):
        with open(file_path) as f:
            data = json.load(f)
    else:
        data = []
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
