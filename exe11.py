#Exercicio 11

# Entrada de dados
salario_antigo = float(input("Digite o salário antes do aumento: "))
novo_salario = float(input("Digite o novo salário: "))

# Cálculo do percentual de aumento
percentual_aumento = ((novo_salario - salario_antigo) / salario_antigo) * 100

# Saída de resultado
print(f"Percentual de aumento: {percentual_aumento:.2f}%")
