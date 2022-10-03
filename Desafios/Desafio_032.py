t = (" Desafio 32 ")
print(f"{t:=^20}")
ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    if ano % 100 != 0:
        print(f"O ano de {ano} é Bissexto!")
    elif ano % 100 == 0 and ano % 400 == 0:
        print(f"O ano de {ano} é Bissexto!")
    else:
        print(f"O ano de {ano} não é Bissexto!")
else:
    print(f"O ano de {ano} não é Bissexto!")