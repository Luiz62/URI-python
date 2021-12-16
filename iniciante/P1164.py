def eh_perfeito(num):
    s = 0
    for i in range(1, num, 1):
        if num % i == 0:
            s += i

    if num == s:
        return True
    return False


qt = int(input())

for i in range(qt):
    n = int(input())
    if eh_perfeito(n):
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')
