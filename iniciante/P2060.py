N = int(input())
valores = []
v1 = [2, 3, 4, 5]
m2 = m3 = m4 = m5 = 0
x = input().split()
for v in x:
    valores.append(int(v))

for valor in valores:
    if valor % 2 == 0:
        m2 += 1
    if valor % 3 == 0:
        m3 += 1
    if valor % 4 == 0:
        m4 += 1
    if valor % 5 == 0:
        m5 += 1
v = [m2, m3, m4, m5]
for i in range(4):
    print(f'{v[i]} Multiplo(s) de {v1[i]}')
