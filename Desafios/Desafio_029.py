t = (" Desafio 29 ")
print(f"{t:=^20}")
vel = float(input("Qual a velocidade o carro passou no radar? "))
if vel > 80:
    multa = (vel - 80) * 7
    print(f"O carro ultrapassou a velidade limite de 80km/h, passando a {vel}km/h, e pagará uma multa no valor de R$ {multa:.2f}")
else:
    print("PARABÉNS! Velocidade dentro do limite da via.")