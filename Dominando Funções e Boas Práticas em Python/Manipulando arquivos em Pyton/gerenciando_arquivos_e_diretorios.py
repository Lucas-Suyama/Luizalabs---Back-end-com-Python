#Gerenciando arquivos e diretórios
#Podemos criar, renomear e excluir arquivos e diretórios
#usando modulos 'os' e 'shutil'
import os
import shutil
from pathlib import Path

ROOT_DIR = Path(__file__).parent

print(ROOT_DIR)

#Criar um arquivo
#os.mkdir(ROOT_DIR / 'arquivos')

#file = open(ROOT_DIR / "novo_arquivo.txt", "w")
#file.write("Hello World!")
#file.close()

#Renomear um arquivo
#os.rename(ROOT_DIR / 'novo_arquivo.txt', ROOT_DIR / 'alterado.txt')

#Excluir um arquivo
#os.remove(ROOT_DIR / 'alterado.txt')

#Mover um arquivo
#shutil.move(ROOT_DIR / 'introducao_arquivos.txt', ROOT_DIR / 'arquivos/introducao_arquivos.txt')
