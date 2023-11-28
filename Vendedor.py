import requests
import json
from util import *
from datetime import datetime 
from pprint import pprint


url = "https://projetofinalpersistenciadados-default-rtdb.firebaseio.com/"

dadosvendedor = {
    "nomeVendedor": "Jocimar Galvão"   
}
# id = "-NkD3KdgfAbaB9lamTTD"


def cria_vendedor(dados):
    requisicao = requests.post(f'{url}/Vendedor/.json', data=json.dumps(dados))
    print(requisicao)
    return requisicao.text

def atualiza_vendedor(dados, id):
    requisicao = requests.patch(f'{url}/Vendedor/{id}/.json', data=json.dumps(dados))
    print(requisicao)
    return requisicao.text

def informa_vendedor():
    requisicao = requests.get(f'{url}/Vendedor.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    return dic_requisicao

def deleta_vendedor(id):
    requisicao = requests.delete(f'{url}/Vendedor/{id}/.json')
    print(requisicao)
    return requisicao.text

# pprint(cria_vendedor(dadosvendedor))
# pprint(atualiza_vendedor(dadosvendedor, id))
# pprint(informa_vendedor())
# pprint(deleta_vendedor(id))

def menu_vendedor():
    print('''
        digite 1 para criar vendedor
        digite 2 para atualizar vendedor
        digite 3 para deletar vendedor
        digite 4 para ver vendedores
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