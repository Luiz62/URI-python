v = [1, 3, 5, 7, 9]
v1 = [7, 6, 5]
s = 0
for x in v:
    for x1 in v1:
        print(f'I={x} J={x1+s}')
    s += 2
