p1 = i1 = p2 = i2 = 0
for x in range(0, 5, 1):
    n = int(input())
    if n > 0:
        p2 += 1
    elif n != 0:
        i2 += 1
    if n % 2 == 0:
        p1 += 1
    else:
        i1 += 1
print(f'{p1} valor(es) par(es)')
print(f'{i1} valor(es) impar(es)')
print(f'{p2} valor(es) positivo(s)')
print(f'{i2} valor(es) negativo(s)')
