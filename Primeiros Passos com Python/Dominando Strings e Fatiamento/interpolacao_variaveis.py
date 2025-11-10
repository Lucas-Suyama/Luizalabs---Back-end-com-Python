#Interpolação de variáveis
#* Substitui um valor por outro em uma string.
#* Utiliza o operador de formatação %
#* Utiliza o método format()
#* Utiliza f-strings

#Utilizando o operador de formatação %
name = 'João'
age = 28
print('Meu nome é %s e tenho %d anos de idade' % (name, age))

#Utilizando o método format()
name = 'Giovana'
age = 24
print('Meu nome é {} e tenho {} anos de idade'.format(name, age))

#Utilizando f-strings
name = 'Lucas'
age = 24
print(f'Meu nome é {name} e tenho {age} anos de idade')