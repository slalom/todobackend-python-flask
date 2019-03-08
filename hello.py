from flask import Flask, request, jsonify
from flask_cors import CORS

arr = [] 

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST", "DELETE"])
def hello():
    if request.method == "GET": 
      print(jsonify(arr))
      return jsonify(arr)
    if request.method == "POST":
      body = request.get_json()
      arr.append(body['title'])
      print(arr)
      return jsonify(body)
    if request.method == "DELETE":
      arr = [] 
      return arr


app.run()