#Indentação
# utilizada para definir o bloco de código
# deve ser consistente em todo o arquivo pois o compilador 
# determina onde o bloco inicia e onde ele termina.

# Blocos de comandos
# são os comandos que são executados quando o bloco é atingido, em outras linguagens utiliza-se chaves {}
# são definidos pela indentação em Python

##Exemplo:
def sacar(valor):
    saldo = 1000
    if valor <= saldo:
        saldo -= valor
        print(f"Saque de {valor} realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

sacar(500)