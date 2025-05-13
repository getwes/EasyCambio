
import requests

def obter_precos():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,solana',
        'vs_currencies': 'usd'
    }

    resposta = requests.get(url, params=params)
    dados = resposta.json()

    linhas = []
    for moeda, valor in dados.items():
        linhas.append(f"{moeda.title()}: ${valor['usd']:.2f}")

    return "\n".join(linhas)