#Exercicio 10

distancia_metros = float(input("Digite a distância em metros: "))
tempo_segundos = float(input("Digite o tempo em segundos: "))

# Conversão de metros para quilômetros
distancia_quilometros = distancia_metros / 1000

# Cálculo da velocidade média em m/s
velocidade_ms = distancia_metros / tempo_segundos

# Cálculo da velocidade média em km/h
velocidade_kmh = (distancia_quilometros / (tempo_segundos / 3600))

print(f"Velocidade média em m/s: {velocidade_ms:.2f} m/s")
print(f"Velocidade média em km/h: {velocidade_kmh:.2f} km/h")
