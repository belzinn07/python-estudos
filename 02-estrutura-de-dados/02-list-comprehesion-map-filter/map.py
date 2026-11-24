#map -> aplica uma função (lambda) a cada elemento da lista
numeros = [10,20,30,40]
dobro = list(map(lambda numero: numero * 2, numeros))
print(f"O dobro de {numeros} é {dobro}")