N = int(input())
X = list()
for i in range(0, N, 1):
    X.append(int(input()))
for n in X:
    if n == 0:
        print('NULL')
    elif n % 2 == 0:
        print('EVEN', end='')
        if n > 0:
            print(' POSITIVE')
        elif n < 0:
            print(' NEGATIVE')
    else:
        print('ODD', end='')
        if n > 0:
            print(' POSITIVE')
        elif n < 0:
            print(' NEGATIVE')