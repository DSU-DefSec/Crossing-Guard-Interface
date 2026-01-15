from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/raise")
def guardRaise():
    pass

@app.route("/lower")
def guardLower():
    pass

app.run(debug=True)