frase = "Curso em Vídeo Python"
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[2:13:3])
print(frase[:13:3])
print(frase[::3])
print(len(frase))
print(frase.upper().count("O"))
print(frase.replace("em", "de"))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
print("_".join(dividido))
print("""Prezada Senhora,
Cumprimentando-a cordialmente, relato a Vossa Senhoria que há uma preocupação institucional referente à segurança contra incêndio, 
explosão e pânico nos estádios de futebol paraibanos, para que atendam as normas de segurança, bem como, as prerrogativas nacionais 
apontadas pela Lei 10.671 - Estatuto do torcedor, de 15 de maio de 2003, 
destacadas em visita realizada na data de 05 de setembro do corrente ano, ao Estádio Governador Ernani Sátiro – 
O Amigão, garantindo assim a incolumidade dos cidadãos.""")