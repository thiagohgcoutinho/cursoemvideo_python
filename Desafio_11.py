t = str(" Desafio 11 ")
print(f"{t:=^20}")
l = float(input("Digite a largura da parede em metros: "))
h = float(input("Digite a altura da parede em metros: "))
a = l * h
print(f"Uma parede com {l}m de largura e {h}m de altura, possuindo uma área de {a:.2f}m2, necessita de {a/2:.0f} litros de tinta.")