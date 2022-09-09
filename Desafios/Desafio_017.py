import math
t = str(" Desafio 17 ")
print(f"{t:=^20}")
co = float(input("Digite o valor do Cateto Oposto: "))
ca = float(input("Digite o valor do Cateto Adjacente: "))
hi = math.hypot(co, ca)
print(f"Para o valor do Cateto Oposto {co} e o Cateto Adjacente {ca}, a Hipotenusa será {hi:.2f}!")