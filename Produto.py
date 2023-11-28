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
        Digite 1 para criar Produto
        Digite 2 para atualizar Produto
        Digite 3 para deletar Produto
        Digite 4 para ver Produtos
        Digite 0 para voltar
    ''')
    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        print("Digite os dados do produto:")
        descricaoProduto: str = input("descricao do Produto: ")
        valorProduto: str = input("valor do Produto: ")

        dados_produto = {
            "descricaoProduto": descricaoProduto,
            "valorProduto": valorProduto    
        }
        return cria_produto(dados_produto)

    elif escolha == "2":
        print("Digite a ID do produto que deseja atualizar:")
        id_produto = input("ID do produto: ")
        if not id:
            print("nenhum id informado")
            return "nenhum id informado"
        
        print("Digite os novos dados do produto:")
        descricaoProduto: str = input("descricao do Produto: ")
        valorProduto: str = input("valor do Produto: ")

        dados_produto = {
            "descricaoProduto": descricaoProduto,
            "valorProduto": valorProduto    
        }
        return atualiza_produto(dados_produto, id_produto)

    elif escolha == "3":
        print("Digite a ID do produto que deseja deletar:")
        id_produto = input("ID do produto: ")
        if not id:
            print("nenhum id informado")
            return "nenhum id informado"
        return deleta_produto(id_produto)

    elif escolha == "4":
        produtos = informa_produto()
        print("Lista de produtos:")
        for id_produto, dados_produto in produtos.items():
            print(f"ID: {id_produto}, descricao: {dados_produto['descricaoProduto']}, valor: {dados_produto['valorProduto']}")
        return "Produtos listados"

    elif escolha == "0":
        return "saiu"
    
    else:
        print("escolha inválida")
        primeiro_menu()