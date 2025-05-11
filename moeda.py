import requests

def converter_moeda(valor, de, para):
    url = f"https://economia.awesomeapi.com.br/json/last/{de}-{para}"
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        raise Exception("Erro ao acessar a API")

    dados = resposta.json()
    chave = f"{de}{para}"
    cotacao = float(dados[chave]["bid"])
    convertido = valor * cotacao

    print(f"{valor:.2f} {de} = {convertido:.2f} {para}")

valor = float(input("Digite o valor: "))
de = input("Moeda de origem (ex: USD): ").upper()
para = input("Moeda de destino (ex: BRL): ").upper()

converter_moeda(valor, de, para)