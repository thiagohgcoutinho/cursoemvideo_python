import random, time
t = (" Desafio 28 ")
print(f"{t:=^20}")
jogador = 0
computador = 1
while jogador != computador:
    computador = random.randint(0, 5)
    jogador = int(input("Qual número o computador escolheu? "))
    print("PROCESSANDO...")
    time.sleep(2)
    if jogador != computador:
        print(f"QUE PENA! Você escolheu {jogador} e o computador escolheu {computador}.")
    else:
        print(f"PARABÉNS! O número escolhido foi {computador}.")