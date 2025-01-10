# # 완전탐색 - 14620번 - 꽃길

n = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []
maps = []
answer = int(1e9)

for _ in range(n):
    maps.append(list(map(int, input().split())))

for i in range(1, n - 1):
    for j in range(1, n - 1):
        result.append((i, j))

for i in combinations(result, 3):
    check(i)

print(answer)
