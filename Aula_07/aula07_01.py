n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2
print(f"A soma vale {s}, \na subtração vale {sub}, \na multiplicação vale {m} \ne a divisão vale {d:.3f}", end=" ")
print(f"A divisão inteira vale {di}, a potência vale {e} e o resto da divisão vale {rd}")