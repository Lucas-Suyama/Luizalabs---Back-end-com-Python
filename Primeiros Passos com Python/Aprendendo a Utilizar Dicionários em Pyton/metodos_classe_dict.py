#Métodos da classe dict
#* A classe dict possui vários métodos úteis.

#.clear
#* Remove todos os elementos do dicionário.
#* Utilizamos o método clear() para remover todos os elementos do dicionário.

pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print(pessoa)
pessoa.clear()
print(pessoa)

#.copy
#* Cria uma cópia do dicionário.
#* Utilizamos o método copy() para criar uma cópia do dicionário.

pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

pessoa_copia = pessoa.copy()
print(pessoa_copia)

#.fromkeys
#* Cria um novo dicionário com as chaves fornecidas e valores padrão.
#* Utilizamos o método fromkeys() para criar um novo dicionário com as chaves fornecidas e valores padrão.
#* Se não fornecemos um valor padrão, o valor padrão será None.

# Exemplo
chaves = ["nome", "idade", "cidade"]
novo_dict = dict.fromkeys(chaves)
print(novo_dict)

# Se fornecemos um valor padrão
novo_dict = dict.fromkeys(chaves, "desconhecido")
print(novo_dict)

#.get
#* Retorna o valor associado à chave fornecida.
#* Utilizamos o método get() para retornar o valor associado à chave fornecida.
#* Se a chave não existir, retornamos None ou um valor padrão fornecido.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print(pessoa.get("nome"))
print(pessoa.get("idade"))
print(pessoa.get("email"))
print(pessoa.get("email", "email não encontrado"))

#.items
#* Retorna uma lista de tuplas contendo as chaves e valores do dicionário.
#* Utilizamos o método items() para retornar uma lista de tuplas contendo as chaves e valores do dicionário.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print(pessoa.items())

#.keys
#* Retorna uma lista contendo as chaves do dicionário.
#* Utilizamos o método keys() para retornar uma lista contendo as chaves do dicionário.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print(pessoa.keys())

#.values
#* Retorna uma lista contendo os valores do dicionário.
#* Utilizamos o método values() para retornar uma lista contendo os valores do dicionário.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print(pessoa.values())

#.pop
#* Remove o elemento com a chave fornecida e retorna o valor associado.
#* Utilizamos o método pop() para remover o elemento com a chave fornecida e retornar o valor associado.
#* Se a chave não existir, retornamos um valor padrão fornecido.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print(pessoa.pop("idade"))
print(pessoa)

#.popitem
#* Remove e retorna o último par chave-valor inserido no dicionário.
#* Utilizamos o método popitem() para remover e retornar o último par chave-valor inserido no dicionário.
#* Se o dicionário estiver vazio, levantamos uma exceção KeyError.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print(pessoa.popitem())
print(pessoa)

#.setdefault
#* Retorna o valor associado à chave fornecida.
#* Se a chave não existir, insere a chave com um valor padrão e retorna o valor padrão.
#* Utilizamos o método setdefault() para retornar o valor associado à chave fornecida.
#* Se a chave não existir, insere a chave com um valor padrão e retorna o valor padrão.
#* Se não fornecemos um valor padrão, o valor padrão será None.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print(pessoa.setdefault("nome", "desconhecido"))
print(pessoa.setdefault("email", "email@email.com"))
print(pessoa)

#.update
#* Atualiza o dicionário com os pares chave-valor fornecidos.
#* Utilizamos o método update() para atualizar o dicionário com os pares chave-valor fornecidos.
#* Se a chave já existir, o valor será atualizado.
#* Se a chave não existir, a chave será inserida com o valor fornecido.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

pessoa.update({"idade": 25, "email": "lucas@email.com"})
print(pessoa)


#in 
#* Verifica se a chave fornecida está presente no dicionário.
#* Utilizamos o operador in para verificar se a chave fornecida está presente no dicionário.
#* Retorna True se a chave estiver presente, False caso contrário.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

print("nome" in pessoa)
print("email" in pessoa)

#del
#* Remove o elemento com a chave fornecida.
#* Utilizamos o comando del para remover o elemento com a chave fornecida.
#* Se a chave não existir, levantamos uma exceção KeyError.

# Exemplo
pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "São Paulo"
}

del pessoa["idade"]
print(pessoa)