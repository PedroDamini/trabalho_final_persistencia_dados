import curses
import requests
import json
from datetime import datetime 
from pprint import pprint
from util import formata_data, formata_e_valida_cpf
from Cliente import cria_cliente, atualiza_cliente, informa_cliente, deleta_cliente, menu_clientes
from Produto import cria_produto, atualiza_produto, informa_produto, deleta_produto, menu_produtos
from Venda import cria_venda, atualiza_venda, informa_venda, deleta_venda, menu_vendas
from Vendedor  import cria_vendedor, atualiza_vendedor, informa_vendedor, deleta_vendedor, menu_vendedor


url = "https://projetofinalpersistenciadados-default-rtdb.firebaseio.com/"

def informa_bd():
    requisicao = requests.get(f'{url}/.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    return dic_requisicao

########################################################################   HOME   ################################################################################################################################################

def primeiro_menu():
    print('''
        digite 1 para manipular clientes
        digite 2 para manipular Produtos
        digite 3 para manipular Vendas
        digite 4 para manipular Vendedor
        digite 5 para Ver Banco de Dados
        digite 0 para sair
    ''')
    escolha1 = input("Digite sua escolha: ")
    
    if escolha1 == "1":
        return menu_clientes()

    elif escolha1 == "2":
        return menu_produtos()

    elif escolha1 == "3":
        return menu_vendas()

    elif escolha1 == "4":
        return menu_vendedor()

    elif escolha1 == "5":
        return pprint(informa_bd())

    elif escolha1 == "0":
        return "saiu"
    
    else:
        print("escolha inválida")
        primeiro_menu()

print(primeiro_menu())
