#Exercicio 9

# Entrada de dados
preco_produto = float(input("Digite o preço do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Cálculo do desconto e novo preço
desconto = (percentual_desconto * preco_produto) / 100
novo_preco = preco_produto - desconto

# Saída de resultados
print(f"Valor do desconto: {desconto:.2f}")
print(f"Novo preço do produto: {novo_preco:.2f}")

# Entrada de dados
preco_produto = float(input("Digite o preço do produto: "))
percentual_aumento = float(input("Digite o percentual de aumento: "))

# Cálculo do aumento e novo preço
aumento = (percentual_aumento * preco_produto) / 100
novo_preco = preco_produto + aumento

# Saída de resultados
print(f"Valor do aumento: {aumento:.2f}")
print(f"Novo preço do produto: {novo_preco:.2f}")
