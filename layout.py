import os

def exibirMenu():
    CONSOLE_SIZE = os.get_terminal_size().columns
    HEADER = " [ BANCO PYTHON ] "
    MENU = """
    \t [ 1 ] - DEPOSITAR
    \t [ 2 ] - SACAR
    \t [ 3 ] - EXIBIR EXTRATO
    \t [ 4 ] - SAIR"""

    print()
    print(HEADER.center(CONSOLE_SIZE, "-"))
    print()
    print(MENU)
    print()