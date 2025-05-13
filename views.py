from main import app
from flask import render_template
from flask import Flask, render_template, request
import requests

#imports do email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#import valor da moeda digital no caso a função
from moeda_digital import obter_precos

precos = obter_precos()

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
    

@app.route("/envia", methods=["POST"])
def enviar_email():
    # Dados do cliente
    nomecliente = request.form["nome"].upper()
    emailcliente = request.form["email"].upper()

    # Buscar preços das criptomoedas
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,solana',
        'vs_currencies': 'usd'
    }
    resposta = requests.get(url, params=params)
    dados = resposta.json()

    precos = ""
    for moeda, valor in dados.items():
        precos += f"{moeda.title()}: ${valor['usd']:.2f}\n"

    # Configuração do e-mail
    mail_remetente = 'ayrtonsenna0110@gmail.com'
    senha = 'fzro zxfk zhnq bfoq'  # Evite deixar senhas no código
    email_destinatario = emailcliente

    mensagem = MIMEMultipart()
    mensagem['From'] = mail_remetente
    mensagem['To'] = email_destinatario
    mensagem['Subject'] = 'Preços Atualizados de Criptomoedas'

    corpo = f"""
    Olá {nomecliente},

    Aqui estão os preços atualizados das criptomoedas:

    {precos}

    Atenciosamente,
    EasyCâmbio
    """

    mensagem.attach(MIMEText(corpo, 'plain'))

    # Enviar e-mail (sem try)
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(mail_remetente, senha)
    servidor.send_message(mensagem)
    servidor.quit()

    print('E-mail enviado com sucesso!')

    return render_template("cadastro_nome_email.html")