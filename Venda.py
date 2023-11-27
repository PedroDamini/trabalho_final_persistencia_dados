import requests
import json
from util import *
from datetime import datetime 
from pprint import pprint


url = "https://projetofinalpersistenciadados-default-rtdb.firebaseio.com/"

dadosvenda = {
    "dataVenda": formata_data(datetime.now()),
    "idCliente": "-NkCAlGlECAnU8uEiY07",
    "idVendedor": "-NkD3KdgfAbaB9lamTTD",
    "idProduto": "-NkD2iQJXXYVc7oL6zjT",
    "valorvenda": "R$115,00"    
}
id = "-NkD2GY81lsSDk3yHSJy"


def cria_venda(dados):
    requisicao = requests.post(f'{url}/Venda/.json', data=json.dumps(dados))
    print(requisicao)
    return requisicao.text

def atualiza_venda(dados, id):
    requisicao = requests.patch(f'{url}/Venda/{id}/.json', data=json.dumps(dados))
    print(requisicao)
    return requisicao.text

def informa_venda():
    requisicao = requests.get(f'{url}/Venda.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    return dic_requisicao

def deleta_venda(id):
    requisicao = requests.delete(f'{url}/Venda/{id}/.json')
    print(requisicao)
    return requisicao.text

# pprint(cria_venda(dadosvenda))
# pprint(atualiza_venda(dadosvenda, id))
# pprint(informa_venda())
# pprint(deleta_venda(id))

