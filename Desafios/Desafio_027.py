t = (" Desafio 27 ")
print(f"{t:=^20}")
nome = str(input("Digite seu nome completo: ")).strip()
div = nome.split()
print(f"Seu primeiro nome é {div[0]}.")
print(f"Seu último nome é {div[len(div) - 1] }.")