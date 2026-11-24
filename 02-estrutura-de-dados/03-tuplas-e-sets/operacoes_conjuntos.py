#Operações de conjuntos
clientes_online = {"João", "Maria", "Carlos", "Ana"}
clientes_loja = {"Pedro", "Maria", "Ana", "José"}

#União -Listando todos os clientes
print(f"Clientes: {clientes_online | clientes_loja}")

#Interseção - Clientes que compram tanto online quanto na loja física.
print(f"\nClientes que compram tanto online quanto na loja física: {clientes_online & clientes_loja}")

#Diferença - Clientes que compram somente na loja online e vice-versa.
print(f"\nCliente que compram apenas na loja online: {clientes_online - clientes_loja}")
print(f"Clientes que compram apenas na loja física: {clientes_loja - clientes_online}")
