t = (" Desafio 22 ")
print(f"{t:=^20}")
nome = input("Digite seu nome completo: ")
print(nome.upper())
print(nome.lower())
print((len(nome)) - (nome.count(" ")))
div = nome.split()
print(len(div[0]))
print(len(nome[0:nome.find(" ")]))