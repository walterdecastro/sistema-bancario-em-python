import os
from layout import *
clear = lambda: os.system("cls")

valor_conta = 0
valor_deposito = 0
valor_saque = 0
LIMITE_SAQUES_DIARIOS = 3
LIMITE_SAQUE_VALOR = 500.00
opt = -1

while opt != 4:
    exibirMenu()
    opt = int(input("\tDigite uma opção: "))
    if opt == 1:
        clear()
        print("\t[ DEPOSITAR ]")
        valor_deposito = float(input("\n\tQual valor gostaria de depositar: "))
        valor_conta += valor_deposito
        clear()
        print(f"\n\tO valor depositado foi: R$ { valor_deposito }\n")
        continue
    elif opt == 2:
        clear()
        print("\t[ SACAR ]")
        valor_saque = float(input("\n\tQual valor gostaria de sacar: "))
        if valor_saque > LIMITE_SAQUE_VALOR:
            print("\n\tTransação não permitida! Valor acima do valor diário.")
        else:
            LIMITE_SAQUES_DIARIOS -= 1
            valor_conta -= valor_saque
            print(f"\n\tO valor sacado foi: R$ { valor_saque }\n")
            print(f"\tVocê ainda poder sacar { LIMITE_SAQUES_DIARIOS } vezes\n")
        continue
    elif opt == 3:
        clear()
        print("\t[ EXTRATO ]")
        print(f"\n\tValor em conta: R$ {valor_conta}")
        print(f"\n\tÚltimo depósito: R$ {valor_deposito}")
        print(f"\n\tÚltimo saque: R$ {valor_saque}")
        continue
    elif opt == 4:
        clear()
        print("[ Obrigado pela preferência | BANCO PYTHON ]".center(os.get_terminal_size().columns, "-"))



