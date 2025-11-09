# Operadores Lógicos
# utilizados para combinar expressões booleanas
# retorna um valor booleano (True ou False)

saldo = 1000
limite = 100
saque = 200
# Operador AND
print(saldo >= saque and saque <= limite)

# Operador OR
print(saldo >= saque or saque <= limite)

# Operador NOT
print(not saldo >= saque)

#Parenteses
print((saldo >= saque) and (saque <= limite))

