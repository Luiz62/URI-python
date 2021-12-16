lista = []
while True:
    nums = list(map(int, input().split()))

    if nums[0] <= 0 or nums[1] <= 0:
        break
    else:
        lista.append(nums.copy())
        nums.clear()
temp = []
for v in lista:
    for i in range(min(v), max(v)+1):
        print(f'{i} ', end='')
        temp.append(i)
    print(f'Sum={sum(temp)}')
    temp.clear()
