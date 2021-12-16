res = []
while True:
    nums = map(int, input().split())
    nums = list(nums)
    if nums[0] == nums[1]:
        break
    else:
        if nums[0] > nums[1]:
            res.append('Decrescente')
        else:
            res.append('Crescente')
for valor in res:
    print(valor)
