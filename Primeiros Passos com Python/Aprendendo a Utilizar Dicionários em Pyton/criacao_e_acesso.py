#Dicionário
#* São coleções desordenadas de elementos.
#* Utilizamos chaves {} para definir um dicionário.
#* Elementos são separados por vírgula.
#* Cada elemento é composto por uma chave e um valor.
#* A chave é utilizada para acessar o valor.

pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print(pessoa)
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

pessoa["email"] = "lucas@email.com"
print(pessoa)

#Dicionarios aninhados
#* Dicionários podem conter outros dicionários.
#* Isso é conhecido como dicionário aninhado.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo",
    "email": "lucas@email.com",
    "telefone": {
        "celular": "123456789",
        "fixo": "987654321"
    }
}

print(pessoa)
print(pessoa["telefone"]["celular"])
print(pessoa["telefone"]["fixo"])

#Iterar sobre um dicionário
#* Podemos iterar sobre as chaves e valores de um dicionário.
#* Utilizamos o método items().
#* O método items() retorna uma lista de tuplas.
#* Cada tupla contém uma chave e um valor.
#* Podemos utilizar o unpacking para separar as chaves e valores.

# Exemplo
for chave, valor in pessoa.items():
    print(chave, valor)