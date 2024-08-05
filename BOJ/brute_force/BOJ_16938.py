# 브루트 포스 - 16938번 - 캠프 준비
from itertools import combinations

n, min_sum, max_sum, min_sub = map(int, input().split())
levels = list(map(int, input().split()))
ans = 0

for i in range(2, n+1):       # 문제 수
    for j in combinations(levels, i):
        arr = list(j)
        if (max(arr)-min(arr) >= min_sub) and (min_sum <= sum(arr) <= max_sum):
            ans += 1

print(ans)