from flask import Flask, render_template, request
from bot import Zeroni
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input", methods=["POST"])
def user_input():
    if request.method == 'POST':
        return str(Zeroni.get_response(request.form["input"]))
