# -*- coding: utf-8 -*-
N = int(input())
X = input().split(' ')
lista = []
for i in range(N):
    lista.append(int(X[i]))

print(f'Menor valor: {min(lista)}')
print(f'Posicao: {lista.index(min(lista))}')
