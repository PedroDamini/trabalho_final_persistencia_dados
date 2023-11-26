import requests
import json
from util import *
from datetime import datetime 
from pprint import pprint


url = "https://projetofinalpersistenciadados-default-rtdb.firebaseio.com/"
# dadosVenda = {
#     "dataVenda": formata_data(datetime.now()),
    
# }

# dadosCliente = {
#     "cpfCliente": formata_e_valida_cpf("89898989898"),
#     "nomeCliente": "Vilson Lira"
# }

# id = "-NkCFnWuf1P5nM--eeM6"

def cria_cliente(dados):
    requisicao = requests.post(f'{url}/Cliente/.json', data=json.dumps(dados))
    print(requisicao)
    return requisicao.text

def atualiza_cliente(dados, id):
    requisicao = requests.patch(f'{url}/Cliente/{id}/.json', data=json.dumps(dados))
    print(requisicao)
    return requisicao.text

def informa_cliente():
    requisicao = requests.get(f'{url}/Cliente.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    return dic_requisicao

def deleta_cliente(id):
    requisicao = requests.delete(f'{url}/Cliente/{id}/.json')
    print(requisicao)
    return requisicao.text

# cria_cliente(dadosCliente)
# atualiza_cliente(dadosCliente, id)
# pprint(informa_cliente())
# pprint(deleta_cliente(id))