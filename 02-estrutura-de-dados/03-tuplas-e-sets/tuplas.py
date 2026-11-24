#Tuplas -> São lista imutáveis, quando os dados representam algo que deve ser mantido fixo
vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")
for p, x in enumerate(vogais):
  print(f"Posição = {p}, valor = {x}")
