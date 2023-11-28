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

def menu_clientes():
    print('''
        digite 1 para criar cliente
        digite 2 para atualizar cliente
        digite 3 para deletar cliente
        digite 4 para ver clientes
        digite 0 para voltar
    ''')
    escolha1 = input("Digite sua escolha: ")
    
    if escolha1 == "1":
        return "escolha 1"

    elif escolha1 == "2":
        return "escolha 2"

    elif escolha1 == "3":
        return "escolha 3"

    elif escolha1 == "4":
        return "escolha 4"

    elif escolha1 == "5":
        return "escolha 5"

    elif escolha1 == "0":
        return "saiu"
    
    else:
        print("escolha inválida")
        primeiro_menu()