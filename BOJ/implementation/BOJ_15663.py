# 구현 - 15663번 - N과 M (9)
import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = set(permutations(list(arr), m))
ans = list(ans)
ans.sort()
# print(ans)
for i in ans:
    for j in i:
        print(j, end=' ')
    print()