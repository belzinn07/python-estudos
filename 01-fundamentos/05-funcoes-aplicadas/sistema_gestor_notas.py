#Defino uma lista de notas vazia para armazenar cada nota inserida pelo usuário
notas = []

#função para calcular média das notas
def calcular_media(soma, notas):
    media = sum(notas)/len(notas)
    return media
#função anônima para arredondar valores com até 2 casas decimais
arredondar = lambda valor: round(valor, 2)
#Inicio do laço de repetição principal
while True:
  print("\n--- Sistemas de Gestão de Notas de Alunos ---")
  print("1 - Registrar Notas")
  print("2 - Sair")
  #captura a opção digitada pelo usuário
  opcao = int(input("Escolha uma opção: "))

  if opcao == 1:

    aluno = input("Digite o nome do aluno: ")
  #loop que executa 4 vezes pedindo a nota ao usuário e indicando a nota correspondente
    notas = []
    for i in range(4):
      nota = float(input(f"Digite a nota {i + 1}: "))
      notas.append(nota)#armazena a nota na lista
    #chama função de calcula média e determina a situação do aluno
    media = calcular_media(sum(notas), notas)
    if media >=7:
      situacao = "Aluno aprovado"
    else:
      situacao = "Aluno reprovado"

    print("\n--- Relatório Final ---")
    print(f"Aluno: {aluno}")
    print("Notas: ")
    #itera sobre cada nota da lista e imprime arredondada para o usuário
    for nota in notas:
        print(arredondar(nota))

    print(f"Média: {arredondar(media)}")
    print(f"Situação: {situacao}")
  #se o usuário digitar 2, encerra o programa
  elif opcao == 2:
    print("Encerrando sistema. Até logo!")
    break;
  #se digitar diferente de 1 ou 2, exibe mensagem de erro.
  else:
    print("Opção inválida! Digite 1 ou 2.")
