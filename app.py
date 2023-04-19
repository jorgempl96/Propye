
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        usu= request.form["txtusuario"]
        passw =request.form["txtpas"]
        print("usuario"+usu+"| password="+passw)
        #consultar con la base de datos
        return render_template("index.html")

@app.route("/Log", methods=['GET', 'POST'])
def Log():
    return render_template("login.html")

