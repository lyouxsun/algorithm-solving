# 구현 - 15654번 - N과 M (5)
from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = list(permutations(arr, m))
result.sort()

for i in result:
    for j in i:
        print(j, end=' ')
    print()

