#Exercicio 14

valor_vista = float(input("Digite um valor a vista: "))
valor_parcelado = float(input("Digite um valor parcelado: "))

# Cálculo do desconto percentual
desconto_percentual = ((1 - valor_vista / valor_parcelado) * 100)

# Saída de resultado
print(f"Desconto percentual para pagamento à vista: {desconto_percentual:.2f}%")
