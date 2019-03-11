from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
arr = []  
@app.route("/", methods=["GET", "POST", "DELETE"])
def hello():
    response = None
    if request.method == "GET": 
        response = jsonify(arr)
    if request.method == "POST":
        body = request.get_json()
        arr.append(body)
        response = jsonify(body)
    if request.method == "DELETE":
        arr.clear()
        response = jsonify(arr)
    print(arr)
    return response

app.run()