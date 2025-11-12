#Decoradores em python
#Inner function - define função dentro de função
def pai():
    print("Pai")
    def filho():
        print("Filho")
    filho()

pai()

#Retornando funções de funções
def calculadora(operacao):
    def soma(a, b):
        return a + b
    def subtracao(a, b):
        return a - b
    def multiplicacao(a, b):
        return a * b
    def divisao(a, b):
        return a / b
    if operacao == "soma":
        return soma
    elif operacao == "subtracao":
        return subtracao
    elif operacao == "multiplicacao":
        return multiplicacao
    elif operacao == "divisao":
        return divisao
    else:
        raise ValueError("Operação inválida")

#Usando a função calculadora
adicao = calculadora("soma")
print(adicao(2, 3))  # Saída: 5

subtracao = calculadora("subtracao")
print(subtracao(5, 2))  # Saída: 3

#Decorador simples - função que recebe outra função como argumento e retorna outra função
def decorador_simples(funcao):
    def wrapper(*args, **kwargs):
        print("Antes da função ser chamada")
        resultado = funcao(*args, **kwargs)
        print("Depois da função ser chamada")
        return resultado
    return wrapper

#Açúcar sintático - forma mais simples de usar decoradores
@decorador_simples
def funcao_exemplo():
    print("Função exemplo sendo chamada")

funcao_exemplo()

#Funções de decoração com argumentos
def decorador_com_argumentos(arg1, arg2):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            print(f"Antes da função ser chamada com argumentos {arg1} e {arg2}")
            resultado = funcao(*args, **kwargs)
            print("Depois da função ser chamada")
            return resultado
        return wrapper
    return decorador

#Usando o decorador com argumentos
@decorador_com_argumentos("a", "b")
def funcao_exemplo_com_argumentos():
    print("Função exemplo com argumentos sendo chamada")

funcao_exemplo_com_argumentos()

#Introspecção - capacidade de um objeto de se inspecionar
def introspecionar(funcao):
    print(f"Nome da função: {funcao.__name__}")
    print(f"Documentação da função: {funcao.__doc__}")
    print(f"Argumentos posicionais da função: {funcao.__code__.co_varnames[:funcao.__code__.co_argcount]}")
    print(f"Argumentos nomeados da função: {funcao.__code__.co_varnames[funcao.__code__.co_argcount:]}")

introspecionar(funcao_exemplo_com_argumentos)