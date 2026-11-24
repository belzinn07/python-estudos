produtos = ["Arroz", "Feijão", "Macarrão"]
produtos_vendidos =   ["Arroz", "Feijão"]

#List Comprehesions -> cria uma nova lista apartir de outra em uma linha
nao_vendidos =  [produto for produto in produtos if produto not in produtos_vendidos]
print("Produtos não vendidos: ")
for produto in nao_vendidos:
    print(f"- {produto}")