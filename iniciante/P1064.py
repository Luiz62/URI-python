p = s = 0
for i in range(6):
    n = float(input())
    if n > 0 and n != 0:
        p += 1
        s += n
print(f'{p} valores positivos')
print(f'{s/p:.1f}')