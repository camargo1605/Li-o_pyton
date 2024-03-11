nac = float(input("Digite sua nota NAC: "))
am = float(input("Digite sua nota AM: "))
ps = float(input("Digite sua nota PS: "))

peso_nac = 2
peso_am = 3
peso_ps = 5

media = (nac * peso_nac + am * peso_am + ps * peso_ps) / (peso_nac + peso_am + peso_ps)

print(f"Média da disciplina: {media:.2f}")

