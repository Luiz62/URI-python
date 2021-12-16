def eh_impar(num):
    if num % 2 != 0:
        return True
    return False


N = int(input())
lista = list()
for i in range(N):
    nums = map(int, input().split())
    lista.append(list(nums))

for v in lista:
    s = 0
    for i in range(min(v)+1, max(v)):
        if eh_impar(i):
            s += i
    print(s)