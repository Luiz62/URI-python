def mdc(x, y):
    return x if not y else mdc(y, x % y)


n = int(input())
for i in range(n):
    n1, n2 = input().split(' ')
    n1, n2 = int(n1), int(n2)
    print(mdc(n1, n2))
