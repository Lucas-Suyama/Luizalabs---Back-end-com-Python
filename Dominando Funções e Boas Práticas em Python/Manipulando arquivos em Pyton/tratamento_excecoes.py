#Exceções mais comuns
#FileNotFoundError - Arquivo não encontrado
#PermissionError - Permissão negada
#IOError - Erro de entrada/saída
#UnicodeDecodeError - Erro de decodificação de caracteres
#UnicodeEncodeError - Erro de codificação de caracteres
#IsADirectoryError - Tentativa de operação em um diretório

try:
    file = open('introducao_arquivos.txt', 'r')
    print(file.read())
    file.close()
except FileNotFoundError as e:
    print('Arquivo não encontrado', e)