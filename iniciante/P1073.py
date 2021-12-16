while True:
    N = int(input())
    if 5 < N < 2000:
        break
i = 2
while i <= N:
    print(f'{i}^{2} = {i**2}')
    i += 2
