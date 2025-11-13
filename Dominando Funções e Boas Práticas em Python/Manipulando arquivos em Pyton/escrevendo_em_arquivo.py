file = open('Dominando Funções e Boas Práticas em Python\Manipulando arquivos em Pyton\introducao_arquivos.txt', 'w')
file.write('Hello World!')
file.writelines(['\n', 'Escrevendo ', 'uma ', 'linha ', 'a ', 'cada ', 'chamada '])
file.close()
