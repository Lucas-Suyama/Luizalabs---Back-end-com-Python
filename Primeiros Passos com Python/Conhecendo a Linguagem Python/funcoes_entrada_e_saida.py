# Função Input
## utilizada quando queremos ler dados de entrada do usuário
## retorna uma string
name = input('Qual é o seu nome? ')
print(name)

#Função Print
## utilizada quando queremos exibir dados na tela
## possui 4 argumentos opcionais
## sep - separador entre os argumentos (padrão é um espaço)
## end - final da linha (padrão é uma quebra de linha)
## file - arquivo de saída (padrão é a saída padrão)
## flush - força a saída imediata (padrão é False)

print(name)
print(name, end='...\n')

