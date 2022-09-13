from random import shuffle
t = (" Desafio 20 ")
print(f"{t:=^20}")
a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f"A ordem escolhida da apresentação será: {lista}!")