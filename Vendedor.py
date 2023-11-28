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

def menu_vendedores():
    print('''
        Digite 1 para criar Vendedor
        Digite 2 para atualizar Vendedor
        Digite 3 para deletar Vendedor
        Digite 4 para ver Vendedores
        Digite 0 para sair
    ''')
    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nomeVendedor: str = input("Digite o nome do vendedor: ")

        dados_vendedor = {
            "nomeVendedor": nomeVendedor  
        }
        return cria_vendedor(dados_vendedor)

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
        return "saindo..."
    
    else:
        print("escolha inválida")
        primeiro_menu()