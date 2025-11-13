import csv
from pathlib import Path

ROOT_DIR = Path(__file__).parent

try:
    with open(ROOT_DIR / 'arquivos/usuarios.csv', 'w', encoding='utf-8') as file:
        csv.writer(file).writerow(['nome', 'email', 'senha'])
        csv.writer(file).writerow(['Lucas', 'lucas@email.com', '123456'])
        csv.writer(file).writerow(['João', 'joao@email.com', '123456'])
        csv.writer(file).writerow(['Maria', 'maria@email.com', '123456'])
except IOError as e:
    print('Erro ao criar arquivo', e)

#práticas recomendadas
#usar csv.reader e csv.writer para ler e escrever arquivos csv
#usar with para garantir que o arquivo será fechado automaticamente
#usar try-except para tratar erros de arquivo
#Ao gravar no arquivo csv, usar newline='' para evitar quebras de linha extras
try:
    with open(ROOT_DIR / 'arquivos/usuarios.csv', 'w', encoding='utf-8', newline='') as file:
        csv.writer(file).writerow(['nome', 'email', 'senha'])
        csv.writer(file).writerow(['Lucas', 'lucas@email.com', '123456'])
        csv.writer(file).writerow(['João', 'joao@email.com', '123456'])
        csv.writer(file).writerow(['Maria', 'maria@email.com', '123456'])
except IOError as e:
    print('Erro ao criar arquivo', e)