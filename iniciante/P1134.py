a = g = d = 0
while True:
    while True:
        cod = int(input())
        if 1 <= cod <= 4:
            break
    if cod == 4:
        break
    else:
        if cod == 1:
            a += 1
        elif cod == 2:
            g += 1
        else:
            d += 1

print('MUITO OBRIGADO')
print(f'Alcool: {a}')
print(f'Gasolina: {g}')
print(f'Diesel: {d}')