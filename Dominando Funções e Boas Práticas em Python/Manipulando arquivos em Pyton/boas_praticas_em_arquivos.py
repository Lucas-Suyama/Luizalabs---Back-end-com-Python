#Bloco with - garante que o arquivo será fechado automaticamente
try:
    with open('introducao_arquivos.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print('Arquivo não encontrado', e)

#Verificar se o arquivo foi aberto com sucesso
try:
    with open('introducao_arquivos.txt', 'r') as file:
        print(file.read())
except IOError as exc:
    print('Erro ao abrir o arquivo', exc)


#Use codificação correta
try:
    with open('introducao_arquivos.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except IOError as exc:
    print('Erro ao abrir o arquivo', exc)