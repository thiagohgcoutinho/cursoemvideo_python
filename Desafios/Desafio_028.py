import random
t = (" Desafio 28 ")
print(f"{t:=^20}")
lista = [0, 1, 2, 3, 4, 5]
n = 0
escolha = 1
while n != escolha:
    escolha = random.choice(lista)
    n = int(input("Qual número o computador escolheu? "))
    if n != escolha:
        print(f"QUE PENA! Você escolheu {n} e o computador escolheu {escolha}.")
    else:
        print(f"PARABÉNS! O número escolhido foi {escolha}.")