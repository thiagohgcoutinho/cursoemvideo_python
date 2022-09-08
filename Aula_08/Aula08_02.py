import random
n1 = random.randint(1, 100)
n2 = int(input("Digite um número entre 1 e 100: "))
if n1<n2:
    print(f"Seu número {n2} foi maior que o do computador, que foi {n1}!")
elif n1>n2:
    print(f"Seu número {n2} foi menor que o do computador, que foi {n1}!")
else:
    print(f"Vocês escolheram o mesmo número {n1}!")