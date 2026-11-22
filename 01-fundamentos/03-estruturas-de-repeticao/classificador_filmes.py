# Programa de classifição de filmes
filmes = ["Toy Story 5","Vingadores","Michael Jackson"]

print("--- Bem vindo a classificação de filmes ---")
print("Avalie os nossos filmes de 1 a 5")
print("Caso deseje parar a digite 0\n")

for filme in filmes:
  while True:
    classificacao = int(input(f"De 1 a 5 que nota o filme '{filme}' merece? "))
    if classificacao == 0:
      print("Avaliação interrompida. Encerrando programa...")
      break
    classificacao = classificacao
    if classificacao < 1 or classificacao > 5:
      print("Nota inválida\n")
    else:
      print(f"{filme} avaliado com {classificacao} estrelas")
      print(f"Obrigado por avaliar o filme {filme}!\n")
      break
