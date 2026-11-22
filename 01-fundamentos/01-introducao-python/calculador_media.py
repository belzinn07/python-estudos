#3. Calcular Média
nome = input("Digite seu nome: ");
print(f"Olá, {nome}! Bem vindo ao Caculador de Média.");

nota_1 =float(input("Digite a nota 1: "));
nota_2 = float(input("Digite a nota 2: "));
nota_3 = float(input("Digite a nota 3: "));
nota_4 = float(input("Digite a nota 4: "));

media = (nota_1 + nota_2 + nota_3 + nota_4)/4;
print("A suá média é ", media);

if media >= 6:
  situacao = "Aprovado"
else:
  situacao = "Reprovado"

print(f"Você está {situacao}");

