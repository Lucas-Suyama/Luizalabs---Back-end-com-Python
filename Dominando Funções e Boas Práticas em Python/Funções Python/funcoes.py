#Funções em Python 
def exibir_mensagem():
    print("Olá, mundo!")

def exibir_mensagem_2(nome):
    print(f"Olá, {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja Bem Vindo, {nome}!")

exibir_mensagem()
exibir_mensagem_2("João")
exibir_mensagem_3()
exibir_mensagem_3("Maria")

def calcular(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

antecessor, sucessor = retorna_antecessor_sucessor(10)
print(antecessor)
print(sucessor)

#Parâmetros especiais
#posicional only, positional or keyword, keyword only.
def criar_carro( modelo, ano, placa, / , marca, motor, combustível):
    print(f"Carro Criado: {modelo}, {ano}, {placa}, {marca}, {motor}, {combustível}")

criar_carro("Civic", 2022, "ABC-1234", marca="Honda", motor="1.8", combustível="Gasolina")
criar_carro("Corolla", 2023, "XYZ-5678", "Toyota", "2.0", "Gasolina")

#Keyword only
def exibir_informacoes(nome, idade, /, *, cidade, estado):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}, Estado: {estado}")

exibir_informacoes("João", 30, cidade="São Paulo", estado="SP")

#Objetos de primeira classe
#Funções são objetos de primeira classe, o que significa que elas podem ser passadas como argumentos para outras funções, retornadas como valores de outras funções e armazenadas em variáveis.
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def operar(a, b, funcao):
    return funcao(a, b)

resultado = operar(5, 3, somar)
print(resultado)

resultado = operar(5, 3, subtrair)
print(resultado)

#Escopo local
#Variáveis definidas dentro de uma função são consideradas locais e não podem ser acessadas fora da função.
def exibir_mensagem():
    mensagem = "Olá, mundo!"
    print(mensagem)

exibir_mensagem()
#print(mensagem) #Erro: mensagem não está definida

#Escopo global
#Variáveis definidas fora de qualquer função são consideradas globais e podem ser acessadas dentro de qualquer função.
mensagem = "Olá, mundo!"

def exibir_mensagem():
    print(mensagem)

exibir_mensagem()
print(mensagem)