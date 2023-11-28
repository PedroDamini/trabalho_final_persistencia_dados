import curses
import requests
import json
from datetime import datetime 
from pprint import pprint
from util import formata_data, formata_e_valida_cpf
from Cliente import cria_cliente, atualiza_cliente, informa_cliente, deleta_cliente
from Produto import cria_produto, atualiza_produto, informa_produto, deleta_produto
from Venda import cria_venda, atualiza_venda, informa_venda, deleta_venda
from Vendedor  import cria_vendedor, atualiza_vendedor, informa_vendedor, deleta_vendedor 


url = "https://projetofinalpersistenciadados-default-rtdb.firebaseio.com/"

def informa_bd():
    requisicao = requests.get(f'{url}/.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    return dic_requisicao

def primeira_escolha(escolha1):
    if escolha1 == "1":
        return "escolha 1"

    elif escolha1 == "2":
        return "escolha 1"

    elif escolha1 == "3":
        return "escolha 1"

    elif escolha1 == "4":
        return "escolha 1"

    elif escolha1 == "5":
        return "escolha 1"

    elif escolha1 == "0":
        return "escolha 1"

########################################################################   HOME   ################################################################################################################################################

print('''
    digite 1 para manipular clientes
    digite 2 para manipular Produtos
    digite 3 para manipular Vendas
    digite 4 para manipular Vendedor
    digite 5 para manipular Ver Banco de Dados
''')

escolha1 = input("Digite sua escolha: ")

primeira_escolha(escolha1)
