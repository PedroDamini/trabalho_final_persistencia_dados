import requests
import json
from util import *
from datetime import datetime 
from pprint import pprint


url = "https://projetofinalpersistenciadados-default-rtdb.firebaseio.com/"

# dadosvenda = {
#     "dataVenda": formata_data(datetime.now()),
#     "idCliente": "-NkCAlGlECAnU8uEiY07",
#     "idVendedor": "-NkD3KdgfAbaB9lamTTD",
#     "idProduto": "-NkD2iQJXXYVc7oL6zjT",
#     "valorVenda": "R$115,00"    
# }
# id = "-NkD2GY81lsSDk3yHSJy"


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
        Digite 1 para criar Venda
        Digite 2 para atualizar Venda
        Digite 3 para deletar Venda
        Digite 4 para ver Vendas
        Digite 0 para sair
    ''')
    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        print("Digite os dados dados Venda:")
        idCliente: str = input("id do cliente: ")
        idVendedor: str = input("id co vendedor: ")
        idProduto: list = input("IDs dos produtos: ")
        valorVenda: str = input("Valor da venda: ")

        dados_venda = {
            "dataVenda": formata_data(datetime.now()),
            "idCliente": idCliente,
            "idVendedor": idVendedor,
            "idProduto": idProduto,
            "valorVenda": valorVenda    
        }
        return cria_venda(dados_venda)

    elif escolha == "2":
        print("Digite a ID da venda que deseja atualizar:")
        id_venda = input("ID do venda: ")
        if not id:
            print("nenhum id informado")
            return "nenhum id informado"
        
        print("Digite os dados dados Venda:")
        idCliente: str = input("id do cliente: ")
        idVendedor: str = input("id co vendedor: ")
        idProduto: list = input("IDs dos produtos: ")
        valorVenda: str = input("Valor da venda: ")

        dados_venda = {
            "dataVenda": formata_data(datetime.now()),
            "idCliente": idCliente,
            "idVendedor": idVendedor,
            "idProduto": idProduto,
            "valorVenda": valorVenda    
        }
        return atualiza_venda(dados_venda, id_venda)

    elif escolha == "3":
        print("Digite a ID do vendedor que deseja deletar:")
        id_vendedor = input("ID do vendedor: ")
        if not id:
            print("nenhum id informado")
            return "nenhum id informado"
        return deleta_vendedor(id_vendedor)
    

    elif escolha == "4":
        vendedores = informa_vendedor()
        print("Lista de vendedores:")
        for id_vendedor, dados_vendedor in vendedores.items():
            print(f"ID: {id_vendedor}, nome: {dados_vendedor['nomeVendedor']}")
        return "vendedores listados"

    elif escolha == "0":
        return "saindo..."
    
    else:
        print("escolha inválida")
        primeiro_menu()