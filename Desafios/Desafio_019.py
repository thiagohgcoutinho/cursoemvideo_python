from random import choice
t = (" Desafio 19 ")
print(f"{t:=^20}")
a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")
lista = [a1, a2, a3, a4]
print(f"O aluno que irá apagar o quadro será {choice(lista)}!")