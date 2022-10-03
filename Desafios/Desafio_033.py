t = (" Desafio 33 ")
print(f"{t:=^20}")
print("Digite três número diferentes!")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(f"O maior número é {n1} e o menor número é {n3}")
        else:
            print(f"O maior número é {n1} e o menor número é {n2}")
    else:
        print(f"O maior número é {n3} e o menor número é {n2}")
else:
    if n2 > n3:
        if n1 > n3:
            print(f"O maior número é {n2} e o menor número é {n3}")
        else:
            print(f"O maior número é {n2} e o menor número é {n1}")
    else:
        print(f"O maior número é {n3} e o menor número é {n1}")