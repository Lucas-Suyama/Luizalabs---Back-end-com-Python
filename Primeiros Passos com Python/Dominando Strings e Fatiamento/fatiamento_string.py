#Fatiamento de strings
#* Permite acessar partes de uma string.
#* Utiliza o operador de fatiamento []

#* Sintaxe: string[início:fim:passo]
#* Início: índice do primeiro caractere a ser acessado.
#* Fim: índice do último caractere a ser acessado.
#* Passo: número de caracteres a ser pulado.


#Exemplo
curso = "Python"

print(curso[0])
print(curso[1:5])
print(curso[1:5:2])
print(curso[::-1])
