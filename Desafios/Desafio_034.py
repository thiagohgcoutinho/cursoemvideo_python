t = (" Desafio 34 ")
print(f"{t:=^20}")
s = float(input("Digite seu salário: "))
if s > 1250:
    a = 0.1 * s
    print(f"Seu salário de R$ {s:.2f} terá um aumento de R$ {a:.2f} passando a ser R$ {(s + a):.2f}")
else:
    a = 0.15 * s
    print(f"Seu salário de R$ {s:.2f} terá um aumento de R$ {a:.2f} passando a ser R$ {(s + a):.2f}")