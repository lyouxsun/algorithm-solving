# 브루트 포스 - 2422번 - 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
from itertools import combinations

n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))
bad = [[False] * (n + 1) for i in range(n + 1)]
for i in arr:
    bad[i[0]][i[1]] = True
    bad[i[1]][i[0]] = True
# print(bad)

comb = list(combinations(range(1, n + 1), 3))
# print('c =', comb)
ans = 0

for i in comb:
    if bad[i[0]][i[1]] or bad[i[1]][i[2]] or bad[i[0]][i[2]]:
        continue
    ans += 1

print(ans)
