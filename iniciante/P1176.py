# -*- coding: utf-8 -*-

m = []

a, b = 0, 1
lista = []
for i in range(0, 60+1):
    lista.append(a)
    a, b = b, a+b


N = int(input())
for i in range(0, N):
    v = int(input())
    m.append(str(f'Fib({v}) = {lista[v]}'))

for valor in m:
    print(valor)