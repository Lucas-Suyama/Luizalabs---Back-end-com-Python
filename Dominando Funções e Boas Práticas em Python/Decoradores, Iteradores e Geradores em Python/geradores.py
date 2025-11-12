#Geradores economiza memoria, pois não armazenam todos os valores na memória, mas geram um por um
#uma vez que um item gerado é consumido, ele é descartado da memória
#o estado interno de um gerador é mantido entre as chamadas de next()
#isso permite que o gerador continue a produzir valores a partir do ponto em que parou
#exemplo:
def meu_gerador():
    for i in range(5):
        yield i

#A execução do gerador é pausada a cada vez que o yield é chamado
#isso permite que o gerador produza valores um por um, sem precisar armazenar todos os valores na memória
#exemplo:
gerador = meu_gerador()
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
#print(next(gerador)) #StopIteration


#Recuperando dados de uma API
#Paginação
#Fornecer um produto por vez

import requests 

def recuperar_produtos(url):
    response = requests.get(url)
    produtos = response.json()
    for produto in produtos:
        yield produto

for produto in recuperar_produtos('https://fakestoreapi.com/products'):
    print(produto)

