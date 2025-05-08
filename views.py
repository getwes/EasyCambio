from main import app
from flask import render_template

#rotas

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/envia_email", methods=["POST"])
def email():
    return render_template("cadastro_nome_email.html")



