def no_intervalo(num):
    if 10 <= num <= 20:
        return True
    return False


N = int(input())
sim = nao = 0
for i in range(N):
    X = int(input())
    if no_intervalo(X):
        sim += 1
    else:
        nao += 1

print(f'{sim} in')
print(f'{nao} out')