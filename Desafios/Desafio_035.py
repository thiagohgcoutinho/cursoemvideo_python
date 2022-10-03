t = (" Desafio 35 ")
print(f"{t:=^20}")
print("Condição de existência de um trinângulo")
r1 = int(input("Digite a primeira reta: "))
r2 = int(input("Digite a segunda reta: "))
r3 = int(input("Digite a terceira reta: "))
if (r1 + r2) > r3:
    if (r1 + r3) > r2:
        if (r2 + r3) > r1:
            print(f"As retas {r1}, {r2} e {r3} formam um triângulo!")
        else:
            print(f"As retas {r1}, {r2} e {r3} não formam um triângulo!")
    else:
        print(f"As retas {r1}, {r2} e {r3} não formam um triângulo!")
else:
    print(f"As retas {r1}, {r2} e {r3} não formam um triângulo!")