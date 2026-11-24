#PDV com estrutura de dados
vendas = [
    {"produto": "Arroz", "quantidade": 2},
    {"produto": "Feijão", "quantidade": 1},
    {"produto": "Arroz", "quantidade": 3},
    {"produto": "Café", "quantidade": 2},
    {"produto": "Feijão", "quantidade": 4}
]

produtos_vendidos = set(item['produto'] for item in vendas)
print(f"Produtos diferentes vendidos: {produtos_vendidos}")

total_produtos = 0
for produto in vendas:
  total_produtos = total_produtos + produto['quantidade']
print(f"Total de produtos vendido: {total_produtos}")

total_arroz = 0
total_feijao = 0
for produto in vendas:
  if produto['produto'] == "Arroz":
    total_arroz = total_arroz + produto['quantidade']
  elif produto['produto'] == "Feijão":
    total_feijao = total_feijao + produto['quantidade']

print(f"Total de arroz vendido {total_arroz}")
print(f"Total de feijão vendido {total_feijao}")

