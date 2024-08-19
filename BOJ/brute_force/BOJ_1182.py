# 브루트 포스 - 1182번 - 부분수열의 합
from itertools import combinations
n, res = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
tmp = []
for i in range(1, n+1):
    tmp.append(list(combinations(arr, i)))
# print(tmp)
for i in tmp:
    for j in i:
        if sum(j) == res:
            cnt += 1

print(cnt)