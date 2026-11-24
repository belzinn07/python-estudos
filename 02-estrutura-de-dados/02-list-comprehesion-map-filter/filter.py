#filter -> separa apenas os elementos que atendem a uma condição
numeros = [10,25,30,45]
pares = list(filter(lambda numero: numero % 2 == 0, numeros))
print(f"Entre os números: {numeros}, os números pares são apenas {pares}")
