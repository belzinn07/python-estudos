#funções anônimas - lambdas
print("--- Calculador de Desconto ---\n")
preco_original = float(input("Digite o preço do produto: "))
valor_porcentagem = float(input("Porcentagem de desconto: "))

converter_porcentagem = lambda valor: valor/100
taxa_desconto = converter_porcentagem(valor_porcentagem)

calcular_desconto = lambda preco, taxa: preco * taxa
valor_desconto = calcular_desconto(preco_original, taxa_desconto)

preco_final = preco_original - valor_desconto
print(f"O preço do produto é {preco_final}")