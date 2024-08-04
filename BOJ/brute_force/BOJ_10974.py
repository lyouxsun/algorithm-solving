# 브루트 포스 - 10974번 - 모든 순열
from itertools import permutations

n = int(input())
arr = [i for i in range(1, n+1)]
arrs = list(permutations(arr, n))
arrs.sort()

for i in arrs:
    for j in i:
        print(j, end=" ")
    print()