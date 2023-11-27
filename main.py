import curses
import requests
import json
from datetime import datetime 
from pprint import pprint
from util import formata_data, formata_e_valida_cpf
from Cliente import cria_cliente, atualiza_cliente, informa_cliente, deleta_cliente
from Produto import cria_produto, atualiza_produto, informa_produto, deleta_produto
from Venda import cria_Venda, atualiza_Venda, informa_Venda, deleta_Venda
from Vendedor  import cria_Vendedor, atualiza_Vendedor, informa_Vendedor, deleta_Vendedor 


url = "https://projetofinalpersistenciadados-default-rtdb.firebaseio.com/"

def informa_bd():
    requisicao = requests.get(f'{url}/.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    return dic_requisicao

########################################################################   HOME   ################################################################################################################################################

print('''
    digite 1 para manipular clientes
    digite 2 para manipular Produtos
    digite 3 para manipular Vendas
    digite 4 para manipular Vendedor
    digite 5 para manipular Ver Banco de Dados
''')