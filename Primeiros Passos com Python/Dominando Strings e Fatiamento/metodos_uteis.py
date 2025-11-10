
curso = "pYtHon"

#Maiusculo
print(curso.upper())

#Minusculo
print(curso.lower())

#Título
print(curso.title())


############################ ELIMINANDO ESPAÇOS EM BRANCO ############################

curso = "            Python            "

#Remover espaços em branco
print(curso.strip())

#Remover espaços à esquerda
print(curso.lstrip())

#Remover espaços à direita
print(curso.rstrip())

############################ JUNÇÕES E CENTRALIZAÇÕS ############################

curso = "Python"

print(curso.center(10, "@"))

#Juntar strings
print("#".join(curso))

