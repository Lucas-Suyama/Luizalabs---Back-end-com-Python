#Iterador - objeto que implementa o método __next__()
#Exemplo de iterador - range()
for i in range(5):
    print(i)


#__init__ - método construtor
#__next__ - método que retorna o próximo elemento do iterador
#__iter__ - método que retorna o iterador
class FileIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')
        self.lines = self.file.readlines()
        self.index = 0
    def __next__(self):
        if self.index >= len(self.lines):
            self.file.close()
            raise StopIteration
        line = self.lines[self.index]
        self.index += 1
        return line
    def __iter__(self):
        return self

for line in FileIterator('test.txt'):
    print(line)

#Outro exemplo:
class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador([1, 2, 3, 4, 5]):
    print(i)