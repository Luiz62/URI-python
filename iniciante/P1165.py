def eh_primo(num):
    qt = 0
    for i in range(2, num):
        if num % i == 0:
            qt += 1

    if qt == 0:
        return True
    return False


j = int(input())

for i in range(j):
    n = int(input())

    if eh_primo(n):
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')
