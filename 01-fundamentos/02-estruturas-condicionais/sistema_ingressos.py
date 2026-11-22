# Sistema de Ingressos de cinema

quantidade_de_ingressos = 100
usuario_cadastrado = "admin"
senha_cadastrada = "admin123"

print("\n" + "="*30)
print("<<< Sistema de Ingressos >>>")
print("\n" + "="*30)

print("Selecione uma opção:")
print("1 - Logar como Admin")
print("2 - Comprar ingressos")
opcao = int(input("Digite o número da opção que deseja: "))

if opcao == 1:
    print("\n--- Login Admin ---")
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print("")
        print("\nLogin realizado com sucesso.\n")
        print("")
        print("Quantidade de ingressos disponíveis: ", quantidade_de_ingressos)
        print("Deseja alterar a quantidade de ingressos?")
        print("1 - Sim")
        print("2 - Não")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            quantidade_de_ingressos = int(input("Digite a nova quantidade: "))
            print("Valor alterado com sucesso!")
            print("Quantidade de ingressos disponíveis:", quantidade_de_ingressos)

        elif escolha == 2:
            print("Quantidade mantida: ", quantidade_de_ingressos)

        else:
            print("Opção inválida. Certifique-se de digitar 1 ou 2")

    else:
        print("Usuário ou senha inválidos")

elif opcao == 2:
    print("\n--- Compra de ingressos ---")

    idade = int( input("Por favor, digite sua idade: "))

    if idade < 12:
      print("Recomendamos o filme Toy Story 5")
    elif idade >= 12 and idade < 18:
      print("Recomendamos o filme Vingadores")
    else:
      print("Recomendamos o filme Michael Jackson")

    print("Quantidade de ingressos disponíveis: ", quantidade_de_ingressos)
    print("\nDeseja comprar ingressos? ")
    print("1 - Sim")
    print("2 - Não")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:

      if quantidade_de_ingressos > 0:
        quantidade_comprada = int(input("Digite a quantidade que deseja comprar: "))
        if quantidade_comprada <= quantidade_de_ingressos and quantidade_comprada > 0:
           print("Compra realizada com sucesso. Divirta-se no cinema!")
           quantidade_de_ingressos = quantidade_de_ingressos - quantidade_comprada
        else:
          print(f"Erro: digite um valor entre 1 e {quantidade_de_ingressos}")

      else:
        print("Desculpe, todos os ingressos estão esgotados para hoje.")

      print("Quantidade de ingressos disponíveis: ", quantidade_de_ingressos)
    elif escolha == 2:
      print("Agradecemos por usar o nosso sistema. Volte sempre!")
    else:
      print("Opção inválida. Certifique-se de digitar 1 ou 2")
else:
    print("Opção inválida. Certifique-se de digitar 1 ou 2")
