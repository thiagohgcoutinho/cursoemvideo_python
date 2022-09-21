t = (" Desafio 23 ")
print(f"{t:=^20}")
num = input("Digite um número entre 0 e 9999: ")
if len(num) == 1:
    print(f"Unidade: {num}")
    print("Dezena: 0")
    print("Centena: 0")
    print("Milhar: 0")
elif len(num) == 2:
    print(f"Unidade: {num[1]}")
    print(f"Dezena: {num[0]}")
    print("Centena: 0")
    print("Milhar: 0")
elif len(num) == 3:
    print(f"Unidade: {num[2]}")
    print(f"Dezena: {num[1]}")
    print(f"Centena: {num[0]}")
    print("Milhar: 0")
else:
    print(f"Unidade: {num[3]}")
    print(f"Dezena: {num[2]}")
    print(f"Centena: {num[1]}")
    print(f"Milhar: {num[0]}")