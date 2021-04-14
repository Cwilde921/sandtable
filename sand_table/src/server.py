from flask import Flask, request, jsonify
from flask_cors import CORS
from Motor import Motor
from config import config
# fetch("http://sandtable.local:5000", {method: "POST", headers:{'Content-Type': 'application/json'}, body: JSON.stringify({}) })

app = Flask(__name__)
CORS(app)

m1 = Motor(config["th_motor_pins_bcm"], True)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        res = { 'a': 123, 'b': 'asf' }
        return jsonify(res)
    else:
        data = request.get_json()
        print(data)
        return "OK"

@app.route("/m1/<steps>")
def motor1(steps):
    m1.walk(int(steps), 0.003)
    return "walked {} steps".format(steps)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
    
