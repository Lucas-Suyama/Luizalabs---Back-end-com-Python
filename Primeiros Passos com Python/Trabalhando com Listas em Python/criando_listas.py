# Criando listas
#* Listas são coleções ordenadas e mutáveis de elementos.
#* Utilizamos colchetes [] para criar listas.
#* Elementos são separados por vírgula.

# Exemplo
frutas = ['maçã', 'banana', 'laranja']
print(frutas)

letras = list("abacate")
print(letras)

numeros = list(range(10))
print(numeros)

#índices negativos
#* Permitem acessar elementos a partir do final da lista.
#* Utilizamos índices negativos para acessar elementos.
#* O índice -1 refere-se ao último elemento da lista.
#* O índice -2 refere-se ao penúltimo elemento da lista.
#* E assim por diante.

print(frutas[-1])
print(letras[-3])
print(numeros[-5:])

#Listas aninhadas
#* Listas podem conter outras listas.
#* Isso é útil para representar estruturas de dados bidimensionais.

# Exemplo
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)

#Acessando elementos de uma lista aninhada
#* Utilizamos dois índices para acessar elementos de uma lista aninhada.
#* O primeiro índice refere-se à lista aninhada.
#* O segundo índice refere-se ao elemento dentro da lista aninhada.

print(matriz[0][2])
print(matriz[2][1])

#Fatiamento de listas
#* Permite acessar uma parte da lista.
#* Utilizamos dois índices para fatiar uma lista.
#* O primeiro índice refere-se ao início do fatiamento.
#* O segundo índice refere-se ao final do fatiamento.
#* O último elemento do fatiamento é excluído.

print(frutas[1:3])
print(letras[2:5])
print(numeros[::2])

#Iterar Listas
#* Permite acessar cada elemento da lista.
#* Utilizamos um loop for para iterar sobre uma lista.

# Exemplo
for fruta in frutas:
    print(fruta)

#Função Enumerate
#* Permite iterar sobre uma lista e obter o índice e o elemento em cada iteração.
#* Utilizamos a função enumerate() para iterar sobre uma lista.

# Exemplo
for indice, fruta in enumerate(frutas):
    print(indice, fruta)

#Compressão de listas
#* Permite criar listas de forma concisa.
#* Utilizamos uma expressão para criar uma lista.
#* A expressão é avaliada para cada elemento da lista.
#* O resultado é uma nova lista com os elementos avaliados.

# Exemplo
quadrados = [x**2 for x in range(10)]
print(quadrados)