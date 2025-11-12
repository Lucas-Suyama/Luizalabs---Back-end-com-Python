import re
from datetime import datetime
from typing import Optional

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

# Log geral das transações realizadas no sistema
transacoes_gerais = []

# Limite de transações diárias (por execução do sistema)
LIMITE_TRANSACOES_DIARIAS = 10
transacoes_por_dia = {}

def _data_hoje_str():
    return datetime.now().strftime("%Y-%m-%d")


def log_transacao(tipo: str):
    """Decorador para logar data/hora e tipo de transação.

    - Print da data/hora e tipo em cada chamada da função decorada.
    - Registro em lista global `transacoes_gerais` com informações básicas.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] Transação: {tipo}")

            resultado = func(*args, **kwargs)

            # Captura melhor esforço do valor da transação
            valor = kwargs.get("valor")
            if valor is None and func.__name__ == "depositar" and len(args) >= 3:
                valor = args[2]

            transacoes_gerais.append(
                {"tipo": tipo, "data_hora": timestamp, "valor": valor}
            )
            return resultado

        return wrapper

    return decorator

@log_transacao("Depósito")
def depositar(saldo, extrato, valor):
    """Realiza depósito se o valor for positivo e atualiza saldo e extrato."""
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

    data_hoje = _data_hoje_str()
    if transacoes_por_dia.get(data_hoje, 0) >= LIMITE_TRANSACOES_DIARIAS:
        print("Operação falhou! Limite diário de 10 transações atingido.")
        return saldo, extrato

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    saldo += valor
    extrato += f"[{timestamp}] Depósito: R$ {valor:.2f}\n"
    transacoes_por_dia[data_hoje] = transacoes_por_dia.get(data_hoje, 0) + 1
    return saldo, extrato

@log_transacao("Saque")
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    """Realiza saque com validações de saldo, limite e quantidade de saques."""
    data_hoje = _data_hoje_str()
    excedeu_transacoes = transacoes_por_dia.get(data_hoje, 0) > LIMITE_TRANSACOES_DIARIAS
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_transacoes:
        print("Operação falhou! Limite diário de 10 transações atingido.")
    elif excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        saldo -= valor
        extrato += f"[{timestamp}] Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        transacoes_por_dia[data_hoje] = transacoes_por_dia.get(data_hoje, 0) + 1
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

@log_transacao("Criação de usuário")
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

@log_transacao("Criação de conta")
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
        # Saldo e transações por conta para uso com iteradores/geradores
        "saldo": 0,
        "transacoes": [],
    }
    contas.append(conta)
    print(f"Conta criada com sucesso. Agência {AGENCIA_PADRAO}, número {numero_conta}.")
    return conta


def gerar_transacoes(transacoes, tipo: Optional[str] = None):
    """Gerador que itera sobre transações e permite filtrar por tipo.

    - `transacoes`: lista de transações (ex.: `transacoes_gerais` ou `conta["transacoes"]`).
    - `tipo`: filtro opcional (ex.: "Depósito" ou "Saque").
    """
    for t in transacoes:
        if tipo is None or (t.get("tipo") or "").lower() == tipo.lower():
            yield t


class ContaIterador:
    """Iterador personalizado para percorrer contas do banco.

    Retorna informações básicas de cada conta: agência, número, usuário e saldo.
    """

    def __init__(self, contas_lista):
        self._contas = contas_lista
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._contas):
            raise StopIteration
        conta = self._contas[self._index]
        self._index += 1
        return {
            "agencia": conta.get("agencia"),
            "numero_conta": conta.get("numero_conta"),
            "usuario": conta.get("usuario", {}).get("nome"),
            "saldo": conta.get("saldo", 0),
        }

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