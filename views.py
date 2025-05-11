from main import app
from flask import render_template
from flask import Flask, render_template, request
import requests
#funcão da moeda
def converter_moeda(valor, de, para):
    url = f"https://economia.awesomeapi.com.br/json/last/{de}-{para}"
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        raise Exception("Erro ao acessar a API")

    dados = resposta.json()
    chave = f"{de}{para}"
    cotacao = float(dados[chave]["bid"])
    convertido = valor * cotacao
    return convertido


#rotas

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/envia_email", methods=["POST"])
def email():
    return render_template("cadastro_nome_email.html")


@app.route("/converter", methods=["POST"])
def converter():
    valor = float(request.form["valor"])
    de = request.form["de"].upper()
    para = request.form["para"].upper()

    
    resultado = converter_moeda(valor, de, para)
    return render_template("home.html", resultado=resultado, de=de, para=para, valor=valor)
    