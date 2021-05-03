from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
try:
    from Motor import Motor
    from config import config
except ModuleNotFoundError:
    from .Motor import Motor
    from .config import config
    
# fetch("http://sandtable.local:5000/api", {method: "POST", headers:{'Content-Type': 'application/json'}, body: JSON.stringify({}) })

app = Flask(__name__)
CORS(app)

@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()
    print(data)
    return "OK"

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        # res = { 'a': 123, 'b': 'asf' }
        return render_template("home.html")
    elif request.method == "POST":
        data = request.get_json()
        print(data)
        return "OK"

# @app.route("/m1/<steps>")
# def motor1(steps):
#     # m1.walk(int(steps), 0.003)
#     return "walked {} steps".format(steps)


# class Server:


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
    
