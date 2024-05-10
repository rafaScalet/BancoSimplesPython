menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao.upper() == "D":
        valor = float(input("\nInforme o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print(f"Operação falhou, o valor {valor:.2f} é inválido")
    elif opcao.upper() == "S":
        valor = float(input("\nInforme o valor do saque: "))
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if valor > saldo:
            print("Operação falhou, saldo insuficiente!")
        elif valor > limite:
            print("Operação falhou, limite insuficiente!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou, limite de saques atingido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print(f"Operação falhou, o valor {valor:.2f} é inválido")
    elif opcao.upper() == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
    elif opcao.upper() == "Q":
        break
    else:
        print(f"Operação '{opcao}' inválida")