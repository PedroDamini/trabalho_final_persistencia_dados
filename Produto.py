import requests
import json
from util import *
from datetime import datetime 
from pprint import pprint


url = "https://projetofinalpersistenciadados-default-rtdb.firebaseio.com/"

dadosproduto = {
    "descricaoProduto": "Teclado mecanico",
    "valorProduto": "R$115,00"    
}
id = "-NkD2GY81lsSDk3yHSJy"


def cria_produto(dados):
    requisicao = requests.post(f'{url}/Produto/.json', data=json.dumps(dados))
    print(requisicao)
    return requisicao.text

def atualiza_produto(dados, id):
    requisicao = requests.patch(f'{url}/Produto/{id}/.json', data=json.dumps(dados))
    print(requisicao)
    return requisicao.text

def informa_produto():
    requisicao = requests.get(f'{url}/Produto.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    return dic_requisicao

def deleta_produto(id):
    requisicao = requests.delete(f'{url}/Produto/{id}/.json')
    print(requisicao)
    return requisicao.text

# pprint(cria_produto(dadosproduto))
# pprint(atualiza_produto(dadosproduto, id))
# pprint(informa_produto())
# pprint(deleta_produto(id))

def menu_produtos():
    print('''
        digite 1 para criar produto
        digite 2 para atualizar produto
        digite 3 para deletar produto
        digite 4 para ver produtos
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