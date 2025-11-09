# Estruturas de Repetição
# são utilizadas para executar um bloco de código várias vezes
# são divididas em dois tipos: while e for
# while é utilizado quando se deseja executar um bloco de código enquanto uma condição for verdadeira
# for é utilizado quando se deseja executar um bloco de código para cada item em uma sequência
#Exemplo:
# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

texto = input("Digite um texto: ")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra)

#Função range
# é utilizada para gerar uma sequência de números
# sintaxe: range(inicio, fim, passo)
#Exemplo:
for i in range(0, 10, 2):
    print(i)