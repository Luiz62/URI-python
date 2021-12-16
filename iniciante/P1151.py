def fibo(num):
    v, v1 = 0, 1
    sla = ''
    for i in range(num):
        sla += str(v) + ' '
        v1, v = v1+v, v1
    lista = ' '.join(sla.split())
    return lista


N = int(input())
lst = fibo(N)
print(lst)
