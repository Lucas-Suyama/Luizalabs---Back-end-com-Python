#Métodos da classe list
#* Permitem realizar operações sobre listas.
#* Utilizamos o operador de ponto . para chamar um método.
#* Cada método é responsável por realizar uma operação específica sobre a lista.

lista = []

#.append
#* Adiciona um elemento ao final da lista.
#* Utilizamos o método append() para adicionar um elemento à lista.

# Exemplo
lista.append(10)
print(lista)

#.clear
#* Remove todos os elementos da lista.
#* Utilizamos o método clear() para remover todos os elementos da lista.

# Exemplo
lista.clear()
print(lista)

#.copy
#* Cria uma cópia da lista.
#* Utilizamos o método copy() para criar uma cópia da lista.

# Exemplo
lista = [1, 2, 3]
copia = lista.copy()
print(copia)

#.count
#* Conta o número de ocorrências de um elemento na lista.
#* Utilizamos o método count() para contar o número de ocorrências de um elemento na lista.

# Exemplo
lista = [1, 2, 3, 2, 1]
print(lista.count(2))

#.extend
#* Adiciona os elementos de uma lista ao final da lista.
#* Utilizamos o método extend() para adicionar os elementos de uma lista ao final da lista.

# Exemplo
lista = [1, 2, 3]
outra_lista = [4, 5, 6]
lista.extend(outra_lista)
print(lista)

#.index
#* Retorna o índice do primeiro elemento encontrado com o valor especificado.
#* Utilizamos o método index() para obter o índice de um elemento na lista.

# Exemplo
lista = [1, 2, 3, 2, 1]
print(lista.index(2))

#.pop
#* Remove o elemento na posição especificada.
#* Utilizamos o método pop() para remover um elemento da lista.

# Exemplo
lista = [1, 2, 3]
removido = lista.pop(1)
print(removido)
print(lista)

#.remove
#* Remove o primeiro elemento encontrado com o valor especificado.
#* Utilizamos o método remove() para remover um elemento da lista.
#* Diferença entre pop e remove:
#* pop() remove um elemento pela posição e retorna o valor removido.
#* remove() remove um elemento pelo valor e não retorna o valor removido.

# Exemplo
lista = [1, 2, 3, 2, 1]
lista.remove(2)
print(lista)

#.reverse
#* Inverte a ordem dos elementos na lista.
#* Utilizamos o método reverse() para inverter a ordem dos elementos na lista.

# Exemplo
lista = [1, 2, 3]
lista.reverse()
print(lista)

#.sort
#* Ordena os elementos da lista.
#* Utilizamos o método sort() para ordenar os elementos da lista.

# Exemplo
linguagens = ['Python', 'Java', 'C++', 'JavaScript']
linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

#.len
#* Retorna o número de elementos na lista.
#* Utilizamos o método len() para obter o número de elementos na lista.

# Exemplo
lista = [1, 2, 3]
print(len(lista))

#.sorted
#* Retorna uma nova lista ordenada.
#* Utilizamos o método sorted() para obter uma nova lista ordenada.
#* Diferença entre sort e sorted:
#* sort() ordena a lista original.
#* sorted() retorna uma nova lista ordenada.

# Exemplo
lista = [3, 1, 2]
print(sorted(lista))