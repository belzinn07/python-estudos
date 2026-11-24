#PDV com Relatório automático
vendas = [
    {"produto": "Arroz", "quantidade": 2},
    {"produto": "Feijão", "quantidade": 1},
    {"produto": "Arroz", "quantidade": 3},
    {"produto": "Café", "quantidade": 2},
    {"produto": "Feijão", "quantidade": 4}
]

resumo = {}

for produto in vendas:
    if not produto['produto'] in resumo:
      resumo[produto['produto']] = produto['quantidade']
    else:
      resumo[produto['produto']] += produto['quantidade']

print("--- Relatório de Vendas ---")
for chave, valor in resumo.items():
        print(f"{chave} : {valor}")
