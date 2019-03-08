from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST", "DELETE"])
def hello():
    if request.method == "GET":
      return "[]"
    if request.method == "POST":
      body = request.get_json()
      return jsonify(body)
    if request.method == "DELETE":
      return ""

app.run()