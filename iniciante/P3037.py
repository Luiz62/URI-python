lista = []
vencedor = []
N = int(input())
for j in range(N):
    pontuacao_joao = pontuacao_maria = 0
    for joao in range(0, 3):
        nums = map(int, input().split())
        nums = list(nums)
        pontuacao_joao += nums[0] * nums[1]

    for maria in range(0, 3):
        nums = map(int, input().split())
        nums = list(nums)
        pontuacao_maria += nums[0] * nums[1]

    if pontuacao_joao > pontuacao_maria:
        vencedor.append('JOAO')
    else:
        vencedor.append('MARIA')

for p in vencedor:
    print(p)