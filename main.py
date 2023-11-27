import curses
import requests
import json
from datetime import datetime 
from pprint import pprint
from util import *
from Cliente import *
from Produto import *
from Venda import *
from Vendedor  import * 


url = "https://projetofinalpersistenciadados-default-rtdb.firebaseio.com/"

def informa_bd():
    requisicao = requests.get(f'{url}/.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    return dic_requisicao

########################################################################   HOME   ################################################################################################################################################

def coletar_dados_cliente(stdscr, cliente_id=None):
    stdscr.clear()

    if cliente_id:
        stdscr.addstr(0, 0, f"Editando cliente com ID: {cliente_id}")
    else:
        stdscr.addstr(0, 0, "Criando novo cliente. Deixe a ID em branco.")

    stdscr.refresh()

    stdscr.addstr(3, 0, "CPF do Cliente:")
    stdscr.refresh()
    cpf_cliente = ""
    while True:
        ch = stdscr.getch()
        if ch == 10:  # Enter key
            break
        elif ch == 127:  # Backspace key
            cpf_cliente = cpf_cliente[:-1]
        else:
            cpf_cliente += chr(ch)
        stdscr.addstr(3, len("CPF do Cliente:"), " " * (stdscr.getmaxyx()[1] - len("CPF do Cliente:") - 1))
        stdscr.addstr(3, len("CPF do Cliente:"), cpf_cliente)
        stdscr.refresh()

    stdscr.addstr(5, 0, "Nome do Cliente:")
    stdscr.refresh()
    nome_cliente = ""
    while True:
        ch = stdscr.getch()
        if ch == 10:  # Enter key
            break
        elif ch == 127:  # Backspace key
            nome_cliente = nome_cliente[:-1]
        else:
            nome_cliente += chr(ch)
        stdscr.addstr(5, len("Nome do Cliente:"), " " * (stdscr.getmaxyx()[1] - len("Nome do Cliente:") - 1))
        stdscr.addstr(5, len("Nome do Cliente:"), nome_cliente)
        stdscr.refresh()

    stdscr.addstr(7, 0, f"ID do Cliente: {cliente_id}")
    stdscr.addstr(8, 0, f"CPF do Cliente: {cpf_cliente}")
    stdscr.addstr(9, 0, f"Nome do Cliente: {nome_cliente}")
    stdscr.refresh()

    return {"idCliente": cliente_id, "cpfCliente": formata_e_valida_cpf(cpf_cliente), "nomeCliente": nome_cliente}




def manipular_cliente(stdscr):
    while True:
        stdscr.clear()

        stdscr.addstr(0, 0, "O que deseja fazer:")
        stdscr.addstr(1, 0, "1. Criar Cliente")
        stdscr.addstr(2, 0, "2. Ler Informações do Cliente")
        stdscr.addstr(3, 0, "3. Atualizar Informações do Cliente")
        stdscr.addstr(4, 0, "4. Excluir Cliente")
        stdscr.addstr(5, 0, "0. Voltar para o Menu Principal")

        escolha_cliente = stdscr.getch()

        if escolha_cliente == ord('1'):
            # Lógica para criar cliente
            dados = coletar_dados_cliente(stdscr)
            resultado = cria_cliente(dados)
            stdscr.addstr(7, 0, f"Resultado da criação: {resultado}. Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

        elif escolha_cliente == ord('2'):
            # Lógica para ler informações do cliente
            informacoes = informa_cliente()
            stdscr.addstr(7, 0, f"Informações do Cliente: {informacoes}. Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

        elif escolha_cliente == ord('3'):
            # Lógica para atualizar informações do cliente
            dados = coletar_dados_cliente(stdscr)
            cliente_id = "ID_do_cliente"  # Substitua pelo ID real do cliente
            resultado = atualiza_cliente(dados, cliente_id)
            stdscr.addstr(7, 0, f"Resultado da atualização: {resultado}. Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

        elif escolha_cliente == ord('4'):
            # Lógica para excluir cliente
            cliente_id = "ID_do_cliente"  # Substitua pelo ID real do cliente
            resultado = deleta_cliente(cliente_id)
            stdscr.addstr(7, 0, f"Resultado da exclusão: {resultado}. Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

        elif escolha_cliente == ord('0'):
            break  # Voltar para o Menu Principal

        else:
            stdscr.addstr(7, 0, "Escolha inválida. Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

def main(stdscr):
    curses.curs_set(0)  # Oculta o cursor
    stdscr.clear()

    while True:
        stdscr.clear()

        stdscr.addstr(0, 0, "O que deseja fazer:")
        stdscr.addstr(1, 0, "1. Visualizar o BD")
        stdscr.addstr(2, 0, "2. Manipular as informações de Cliente")
        stdscr.addstr(3, 0, "3. Manipular as informações de Vendas")
        stdscr.addstr(4, 0, "4. Manipular as informações de Produto")
        stdscr.addstr(5, 0, "5. Manipular as informações de Vendedor")
        stdscr.addstr(6, 0, "0. Sair")

        escolha = stdscr.getch()

        if escolha == ord('1'):
            stdscr.addstr(8, 0, "Visualizando o BD... Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

        elif escolha == ord('2'):
            manipular_cliente(stdscr)

        elif escolha == ord('3'):
            stdscr.addstr(8, 0, "Manipulando as informações de Vendas... Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

        elif escolha == ord('4'):
            stdscr.addstr(8, 0, "Manipulando as informações de Produto... Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

        elif escolha == ord('5'):
            stdscr.addstr(8, 0, "Manipulando as informações de Vendedor... Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

        elif escolha == ord('0'):
            break  # Sair do programa

        else:
            stdscr.addstr(8, 0, "Escolha inválida. Pressione qualquer tecla para continuar.")
            stdscr.refresh()
            stdscr.getch()

curses.wrapper(main)
