#funções definidas pelo usuário
notas = [10,8.4,9.75,8.9]
soma = sum(notas)
def calcular_media(soma, notas):
  media = soma/len(notas)
  return media
media = calcular_media(soma, notas)
print(f"A média é {media}")