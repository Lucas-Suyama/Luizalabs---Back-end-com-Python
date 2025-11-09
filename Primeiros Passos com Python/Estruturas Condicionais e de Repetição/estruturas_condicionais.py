# Estruturas Condicionais
# utilizadas para tomar decisões com base em condições
# são definidas pela indentação em Python

#Exemplo

saldo = 1000
saque = 100
if saque <= saldo:
    saldo -= saque
    print(f"Saque de {saque} realizado com sucesso!")
else:
    print("Saldo insuficiente!")

#Exemplo com mais de uma condição
#Elif é utilizado para verificar outra condição se a primeira não for atendida
#Else é utilizado para verificar se nenhuma das condições anteriores for atendida
saldo = 1000
saque = 100
if saque <= saldo:
    saldo -= saque
    print(f"Saque de {saque} realizado com sucesso!")
elif saque <= 500:
    print("Saque acima do limite máximo permitido!")
else:
    print("Saldo insuficiente!")

#If ternário
# é uma forma compacta de escrever um if-else
# sintaxe: valor_se_verdadeiro if condicao else valor_se_falso
#Exemplo:
saldo = 1000
saque = 100
mensagem = "Saque realizado com sucesso!" if saque <= saldo else "Saldo insuficiente!"
print(mensagem)
