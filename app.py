from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

message = "raised"

@app.route("/")
def index():
    return render_template("index.html", message=message)

@socketio.on("raise")
def guardRaise():
    global message
    message = "raised"
    emit("raised", message, broadcast=True, namespace="/")

@socketio.on("lower")
def guardLower():
    global message
    message = "lowered"
    emit("lowered", message, broadcast=True, namespace="/")

socketio.run(app, debug=True)