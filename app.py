from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/raise")
def guardRaise():
    emit("raise", "raised", broadcast=True, namespace="/")
    return "raised"

@app.route("/lower")
def guardLower():
    emit("lower", "lowered", broadcast=True, namespace="/")
    return "lowered"

socketio.run(app, debug=True)