menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} (+)\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Qual o valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Operação falhou! Você não tem saldo suficiente.\nSaldo: R$ {saldo:.2f}")

        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite.\nLimite: R$ {limite:.2f}")

        elif excedeu_saques:
            print(f"Operação falhou! Número máximo de saques excedido.\nSaques: {numero_saques} de {LIMITE_SAQUES} saques permitidos no dia.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} (-)\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f} (+)")
        print("========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")