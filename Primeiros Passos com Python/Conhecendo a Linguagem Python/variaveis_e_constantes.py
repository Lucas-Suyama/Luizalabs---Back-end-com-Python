# Variaveis - Armazena valores que podem sofrer alterações no decorrer da execução do programa.
age = 24
name='Lucas'
print(f'Meu nome é {name} e tenho {age} anos de idade')

age, name = (17, 'João')
print(f'Meu nome é {name} e tenho {age} anos de idade')

#Constantes - Armazena valores que não sofrerão alterações no decorrer da execução do programa.
#* Não existe palavra reservada para declarar constantes em Python.
#* Para isso, uma constante é declarada com letras maiúsculas.
PI = 3.14159

#Boas práticas
#* Padrão de nomes deve ser em snake case - (valor_total, taxa_juros)
#* Escolher nomes sugestivos
#* Nome de constantes em Maiúsculo

nome = 'João'
idade = 28

nome = 'Giovana'

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ['SP', 'RJ', 'MG', 'ES']