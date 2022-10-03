t = (" Desafio 31 ")
print(f"{t:=^20}")
dist = float(input("Digite a distância entre as cidades: "))
if dist <= 200:
    v = 0.5 * dist
    print(f"O valor da passagem para uma viagem de {dist}km é R$ {v:.2f}")
else:
    v = 0.45 * 200
    print(f"O valor da passagem para uma viagem de {dist}km é R$ {v:.2f}")