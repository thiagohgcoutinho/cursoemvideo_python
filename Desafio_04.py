from curses.ascii import isalnum


n = input('Digite algo: ')
print('O tipo primitivo é ', type(n))
print('Só tem espaços: ', n.isspace())
print('É um número: ', n.isnumeric())
print('É alfabético: ', n.isalpha())
print('É alfanumérico: ', n.isalnum())
print('Está maiúscula: ', n.isupper())
print('Está minúscula: ', n.islower())
print('Está captalizada: ', n.istitle())
print(f'O tipo primitivo é {type(n)}, tem espaços: {n.isspace()}, é um número: {n.isnumeric()}, está captalizada: {n.istitle()}.')