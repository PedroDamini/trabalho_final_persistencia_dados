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
    if id:
        requisicao = requests.patch(f'{url}/Cliente/{id}/.json', data=json.dumps(dados))
        print(requisicao)
        return requisicao.text
    else:
        return "nenhum id informado"

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
        Digite 1 para criar cliente
        Digite 2 para atualizar cliente
        Digite 3 para deletar cliente
        Digite 4 para ver clientes
        Digite 0 para sair
    ''')
    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        print("Digite os dados do cliente:")
        cpf_cliente: str = input("CPF do cliente: ")
        nome_cliente: str = input("Nome do cliente: ")

        dados_cliente = {
            "cpfCliente": formata_e_valida_cpf(cpf_cliente),
            "nomeCliente": nome_cliente
        }
        return cria_cliente(dados_cliente)

    elif escolha == "2":
        print("Digite a ID do cliente que deseja atualizar:")
        id_cliente = input("ID do cliente: ")
        if not id:
            print("nenhum id informado")
            return "nenhum id informado"
        
        print("Digite os novos dados do cliente:")
        cpf_cliente: str = input("Novo CPF do cliente: ")
        nome_cliente: str = input("Novo nome do cliente: ")

        dados_cliente = {
            "cpfCliente": formata_e_valida_cpf(cpf_cliente),
            "nomeCliente": nome_cliente
        }
        return atualiza_cliente(dados_cliente, id_cliente)

    elif escolha == "3":
        print("Digite a ID do cliente que deseja deletar:")
        id_cliente = input("ID do cliente: ")
        if not id:
            print("nenhum id informado")
            return "nenhum id informado"
        return deleta_cliente(id_cliente)

    elif escolha == "4":
        clientes = informa_cliente()
        print("Lista de clientes:")
        for id_cliente, dados_cliente in clientes.items():
            print(f"ID: {id_cliente}, CPF: {dados_cliente['cpfCliente']}, Nome: {dados_cliente['nomeCliente']}")
        return "Clientes listados"

    elif escolha == "0":
        return "saindo..."
    
    else:
        print("escolha inválida")
        primeiro_menu()