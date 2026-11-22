def calcular_desconto(preco, percentual):
  if percentual < 0 or percentual > 100:
    return None

  desconto = preco * (percentual/100)
  return preco - desconto

def registrar_venda(produto, preco):
  print(f"\nVenda registrada: Produto: {produto} | Preço: {preco:.2f}")

arredondar = lambda valor: round(valor, 2)

total_vendas = 0
quantidade_vendas = 0
lista_produtos = []

while True:
  print("\n--- MeuPDV Python ---")
  print("1 - Iniciar Venda")
  print("2 - Relatório do dia")
  print("0 - Encerrar Caixa")
  opcao = int(input("Escolha uma opção: "))

  if opcao == 0:
   print("\nEncerrando caixa. Até logo!")
   break

  elif opcao == 1:
    print("\n--- Venda ---")
    produto = input("Nome do Produto: ")
    preco = float(input("Preço: R$ "))
    percentual = float(input("Desconto (%): "))
    preco_final = calcular_desconto(preco, percentual)

    if preco_final is None:
      print("Desconto inválido! Informe um valor ente 0 e 100")
    else:
      preco_final = arredondar(preco_final)
      registrar_venda(produto, preco_final)
      lista_produtos.append(produto)
      total_vendas = total_vendas + preco_final
      quantidade_vendas = quantidade_vendas + 1

  elif opcao == 2:
    print("\n--- Vendas do dia ---")
    print(f"Quantidade de Vendas: {quantidade_vendas}")
    print(f"Total Faturado: R$ {arredondar(total_vendas)}")

    print("\n--- Produtos Vendidos ---")
    if len(lista_produtos) == 0:
      print("Nenhum produto vendido até o momento.")
    else:
      for produto in lista_produtos:
        print(produto)

  else:
    print("Opção inválida! Certifique de escolher 1,2 ou 0")

