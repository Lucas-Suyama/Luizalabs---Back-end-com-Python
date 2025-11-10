#Tuplas
#* São coleções ordenadas e imutáveis de elementos.
#* Utilizamos parênteses () para definir uma tupla.
#* Elementos são separados por vírgula.

# Exemplo
tupla = (1, 2, 3)
print(tupla)

frutas = ('maçã', 'banana', 'laranja')
print(frutas)

letras = tuple("Python")
print(letras)

numeros = tuple([1, 2, 3])
print(numeros)

pais=("Brasil",)
print(pais)

#Acesso a elementos
#* Utilizamos o operador de fatiamento [] para acessar elementos da tupla.
#* Início: índice do primeiro caractere a ser acessado.
#* Fim: índice do último caractere a ser acessado.
#* Passo: número de caracteres a ser pulado.

#tupla aninhada
#* Tuplas podem conter outras tuplas.
#* Isso é conhecido como tupla aninhada.

# Exemplo
tupla_aninhada = (1, 2, (3, 4, 5))
print(tupla_aninhada)

#Acesso a elementos aninhados
#* Utilizamos o operador de fatiamento [] para acessar elementos aninhados.
#* Início: índice do primeiro caractere a ser acessado.
#* Fim: índice do último caractere a ser acessado.
#* Passo: número de caracteres a ser pulado.

# Exemplo
print(tupla_aninhada[2])
print(tupla_aninhada[2][1])

#Metodos da classe tuple
#* count()
#* Retorna o número de vezes que um valor específico aparece na tupla.

# Exemplo
print(tupla.count(2))

#index()
#* Retorna o índice do primeiro elemento com o valor especificado.

# Exemplo
print(tupla.index(3))

#.len
#* Retorna o número de elementos na tupla.

# Exemplo
print(len(tupla))