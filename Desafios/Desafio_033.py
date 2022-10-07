t = (" Desafio 33 ")
print(f"{t:=^20}")
print("Digite três número diferentes!")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
'''if n1 > n2:
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
        print(f"O maior número é {n3} e o menor número é {n1}")'''
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

print(f"O menor número é {menor} e o maior é {maior}")