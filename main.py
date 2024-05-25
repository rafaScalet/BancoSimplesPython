def deposito(saldo, extrato, /):
    valor = float(input("\nInforme o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito realizado com sucesso!\nValor: R${valor:.2f}, Saldo: {saldo:.2f}")
    else:
        print(f"\nOperação falhou, o valor {valor:.2f} é inválido")
    return saldo, extrato

def saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("\nInforme o valor do saque: "))
    if valor > saldo:
        print("\noperação falhou saldo insuficiente!")
    elif valor > limite:
        print("\nOperação falhou, limite insuficiente!")
    elif numero_saques >= limite_saques:
        print("\nOperação falhou, limite de saques atingido!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque realizado com sucesso!\nValor: R${valor:.2f}, Saldo: R${saldo:.2f}")
    else:
        print(f"\nOperação falhou, o valor {valor:.2f} é inválido")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, /, *, extrato):
    print("\n=================== EXTRATO ==================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==============================================")

def criar_usuario(usuarios):
    cpf = input("\nCPF (Somente Números):")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nUsuário já existente!")
    else:
        nome = input("Nome completo: ")
        data_nascimento = input("Data de nascimento: ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla do estado): ")
        
        usuarios.append({"CPF": cpf, "nome": nome, "aata_nascimento": data_nascimento, "endereco": endereco})
        print("Usiário criado!")
    return True

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print ("\nUsuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        ========== Contas ==========
        Agência: {conta["agencia"]}
        C/C: {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
        ============================
        """
        print(linha)

menu = """
==================== Menu ====================
[D] Depositar
[S] Sacar
[E] Extrato
[C] Nova Conta
[U] Criar Usuário
[L] Listar Contas
[Q] Sair
==============================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
agencia = "0001"
limite_saques = 3
usuarios = []
contas = []

while True:
    opcao = input(menu)
    if opcao.upper() == "D":
        saldo, extrato = deposito(saldo, extrato)
    elif opcao.upper() == "S":
        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=limite_saques
        )
    elif opcao.upper() == "E":
        mostrar_extrato(saldo, extrato=extrato)
    elif opcao.upper() == "C":
        numero_conta = len(contas) + 1
        conta = criar_conta(agencia, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao.upper() == "U":
        criar_usuario(usuarios)
    elif opcao.upper() == "L":
        listar_contas(contas)
    elif opcao.upper() == "Q":
        break
    else:
        print(f"Operação '{opcao}' inválida")