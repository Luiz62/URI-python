# -*- coding: utf-8 -*-
var = 20
N = []
for i in range(var):
    N.append(int(input()))

N = N[::-1]

for i in range(var):
    print(f'N[{i}] = {N[i]}')
