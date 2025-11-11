import re

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[c] Nova conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA_PADRAO = "0001"

usuarios = []
contas = []

def depositar(saldo, extrato, valor):
    """Realiza depósito se o valor for positivo e atualiza saldo e extrato."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    """Realiza saque com validações de saldo, limite e quantidade de saques."""
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, *, extrato):
    """Exibe o extrato de movimentações e o saldo atual.
    Argumentos posicionais: saldo; argumentos nomeados: extrato.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def limpar_cpf(cpf: str) -> str:
    """Remove caracteres não numéricos do CPF."""
    return re.sub(r"\D", "", cpf)

def encontrar_usuario_por_cpf(usuarios, cpf_limpo):
    """Retorna o usuário com o CPF informado ou None."""
    for usuario in usuarios:
        if usuario["cpf"] == cpf_limpo:
            return usuario
    return None

def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    """Cria um usuário com CPF único e adiciona à lista de usuários."""
    cpf_limpo = limpar_cpf(cpf)
    if encontrar_usuario_por_cpf(usuarios, cpf_limpo):
        print("Operação falhou! Já existe usuário com esse CPF.")
        return False

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_limpo,
        "endereco": endereco,
    }
    usuarios.append(usuario)
    print("Usuário criado com sucesso.")
    return True

def criar_conta(contas, usuarios, cpf):
    """Cria uma conta para o usuário identificado pelo CPF e adiciona à lista de contas."""
    cpf_limpo = limpar_cpf(cpf)
    usuario = encontrar_usuario_por_cpf(usuarios, cpf_limpo)
    if not usuario:
        print("Operação falhou! Usuário não encontrado. Cadastre o usuário primeiro.")
        return None

    numero_conta = len(contas) + 1
    conta = {
        "agencia": AGENCIA_PADRAO,
        "numero_conta": numero_conta,
        "usuario": usuario,
    }
    contas.append(conta)
    print(f"Conta criada com sucesso. Agência {AGENCIA_PADRAO}, número {numero_conta}.")
    return conta

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, extrato, valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES,
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        nome = input("Informe o nome: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        cpf = input("Informe o CPF: ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        criar_conta(contas, usuarios, cpf)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione novamente a opção desejada.")
        print("Operação inválida, por favor selecione novamente a operação desejada.")