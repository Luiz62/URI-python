inter = gremio = empate = count = 0
while True:
    nums = list(map(int, input().split()))
    count += 1
    if nums[0] == nums[1]:
        empate += 1
    elif nums[0] > nums[1]:
        inter += 1
    else:
        gremio += 1
    nums.clear()
    r = int(input('Novo grenal (1-sim 2-nao)\n'))
    if r == 2:
        break
print(f'{count} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')
if inter == gremio:
    print('Nao houve vencedor')
elif inter > gremio:
    print('Inter venceu mais')
else:
    print('Gremio venceu mais')
