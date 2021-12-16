def fact(num):
    f = 1
    for i in range(num, 0, -1):
        f *= i

    return f


N = int(input())
print(fact(N))
