from flask import Flask, request, jsonify
from flask_cors import CORS

# fetch("http://sandtable.local:5000", {method: "POST", headers:{'Content-Type': 'application/json'}, body: JSON.stringify({}) })

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        res = { 'a': 123, 'b': 'asf' }
        return jsonify(res)
    else:
        data = request.get_json()
        print(data)
        return "OK"

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
    
