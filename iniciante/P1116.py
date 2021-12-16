qt = int(input())
resu = []
for i in range(qt):
    nums = map(int, input().split())
    nums = list(nums)
    if nums[0] == 0:
       resu.append('0.0')
    elif nums[1] == 0:
        resu.append('divisao impossivel')
    else:
        resu.append(nums[0]/nums[1])

for v in resu:
    print(v)
