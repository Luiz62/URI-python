res = []
while True:
    nums = map(int, input().split())
    nums = list(nums)
    if nums[0] == 0 or nums[1] == 0:
        break
    else:
        if nums[0] > 0 and nums[1] > 0:
            res.append('primeiro')
        elif nums[0] < 0 and nums[1] < 0:
            res.append('terceiro')
        elif nums[0] < 0 < nums[1]:
            res.append('segundo')
        else:
            res.append('quarto')

for v in res:
    print(v)