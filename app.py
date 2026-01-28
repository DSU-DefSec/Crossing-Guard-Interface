from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import hashlib

app = Flask(__name__)
socketio = SocketIO(app)

message = "raised"
password = "easy password"
phash = hashlib.sha256(bytes(password, encoding="utf-8")).hexdigest()

def verifyPassword(passw):
    return hashlib.sha256(bytes(passw, encoding='utf-8')).hexdigest() == phash

@app.route("/")
def index():
    return render_template("index.html", message=message, phash=phash)

@app.route("/raise", methods=["POST"])
def guardRaise():
    global message
    data = request.json
    if "password" in data and verifyPassword(data["password"]):
        message = "raised"
        emit("raised", message, broadcast=True, namespace="/")
        return "raised"
    return "incorrect password"

@app.route("/lower", methods=["POST"])
def guardLower():
    global message
    data = request.json
    if "password" in data and verifyPassword(data["password"]):
        message = "lowered"
        emit("lowered", message, broadcast=True, namespace="/")
        return "lowered"
    else:
        return "incorrect password"

socketio.run(app, debug=True)