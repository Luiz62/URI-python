valores = input().split()
lista = []

for valor in valores:
    lista.append(float(valor))

triangulo = False
if lista[0] < lista[1] + lista[2]:
    if lista[1] < lista[0] + lista[2]:
        if lista[2] < lista[0] + lista[1]:
            triangulo = True
if triangulo:
    print(f'Perimetro = {sum(lista):.1f}')
else:
    area = ((lista[0] + lista[1]) * lista[2]) / 2
    print(f'Area = {area:.1f}')