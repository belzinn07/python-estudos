#Dict -  associa chave -> valor
produto = {
    "codigo": 777,
    "nome": "Moto G15",
    "preco": 600,
    "estoque": 1
}

print(f"Nome: {produto['nome']}")
print(f"Preço {produto['preco']}")

produto['preco'] = 500
print(f"Novo Preço: {produto['preco']}")
produto['estoque'] = 2
print(f"Novo estoque: {produto['estoque']}")

produto['categoria'] = "Smartphones"
print(produto)