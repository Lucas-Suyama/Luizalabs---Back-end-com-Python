file = open('Dominando Funções e Boas Práticas em Python\Manipulando arquivos em Pyton\introducao_arquivos.txt', 'r')

#read - lê o conteúdo do arquivo
#readline - lê uma linha do arquivo
#readlines - lê todas as linhas do arquivo

print(file.read())
#print(file.readline())
#print(file.readlines())

file.close()