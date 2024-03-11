#Exercício 3

# Solicita o nome e ano de nascimento do usuário
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))

#Calcule a idade até o final de 2024
ano_atual = 2024
idade = ano_atual - ano_nascimento

# Exibe o nome e idade na tela
print("Nome:", nome) 
print("até o fim de 2024 tem ou terá",idade,"anos")