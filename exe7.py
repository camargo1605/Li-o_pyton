#Exercicio 7

def obter_digitos_dezenas_unidades(numero):
    # Verifica se o número está no intervalo de 0 a 99
    if 0 <= numero <= 99:
        # Calcula o dígito das dezenas e o dígito das unidades
        dezenas = numero // 10
        unidades = numero % 10

        # Imprime os resultados
        print(f'Dígito das dezenas: {dezenas}')
        print(f'Dígito das unidades: {unidades}')
    else:
        print('O número fornecido está fora do intervalo de 0 a 99.')

numero_input = int(input('Digite um número de 0 a 99: '))
obter_digitos_dezenas_unidades(numero_input)
