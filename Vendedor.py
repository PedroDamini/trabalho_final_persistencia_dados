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
        print("Digite a ID do vendedor que deseja atualizar:")
        id_vendedor = input("ID do vendedor: ")
        if not id:
            print("nenhum id informado")
            return "nenhum id informado"
        
        nomeVendedor: str = input("Digite o nome do vendedor: ")

        dados_vendedor = {
            "nomeVendedor": nomeVendedor  
        }
        return atualiza_vendedor(dados_vendedor, id_vendedor)

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