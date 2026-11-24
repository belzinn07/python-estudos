#Sets -> é uma coleção de valores únicos, sem repetições
codigos = [101, 102, 101, 103, 104, 102, 105, 103]
unicos = set(codigos)
print(unicos)

codigo = 102
if codigo in unicos:
  print(f"Código {codigo} está presente")
else:
  print(f"Código {codigo} não está presente")

unicos.add(106)
unicos.remove(101)
print(unicos)


