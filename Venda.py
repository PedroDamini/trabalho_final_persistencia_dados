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

def menu_vendas():
    print('''
        digite 1 para criar venda
        digite 2 para atualizar venda
        digite 3 para deletar venda
        digite 4 para ver vendas
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