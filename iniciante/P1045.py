lista = []
valores = input().split()

for valor in valores:
    lista.append(float(valor))
lista.sort(reverse=True)

a, b, c = lista[0], lista[1], lista[2]
if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if (a ** 2) == (b ** 2 + c ** 2):
        print('TRIANGULO RETANGULO')
    if (a ** 2) > (b ** 2 + c ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (a ** 2) < (b ** 2 + c ** 2):
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    if (a == b and b != c) or (b == c and b != a)\
            or (c == a and c != b):
        print('TRIANGULO ISOSCELES')
