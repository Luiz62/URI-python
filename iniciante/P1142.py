N = int(input())

x = 1
for i in range(N):
    for j in range(3):
        print(f'{x} ', end='')
        x += 1
    print('PUM')
    x += 1

