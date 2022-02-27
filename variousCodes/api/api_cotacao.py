# Awesome API

import requests
import json

cotacao = requests.get(url='https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao_moedas = cotacao.json()
cotacao_usd_brl = cotacao_moedas['USDBRL']['bid']
print(f'Cotacao USD/BRL: $ {cotacao_usd_brl}')