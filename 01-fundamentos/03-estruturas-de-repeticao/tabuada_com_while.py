#While
#tabuada de multiplicação
fator = 0
print("\n" + "="*20)
print(" --- TABUADA ---")
print("="*20)
numero_multiplicado = int(input("\nDigite o número tabuada você quer ver: "))
print(f"\n === Tabuada do {numero_multiplicado} ===\n")
while fator <= 20:
  produto = numero_multiplicado * fator
  print(f"{numero_multiplicado} * {fator} = {produto}")
  fator = fator + 1
