# 누적합 - 30461번 - 낚시
import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
arr = []

for i in range(n):
    line = list(map(int, input().split()))
    if i > 0:
        for j in range(m):
            line[j] += arr[i - 1][j]
    arr.append(line)

for i in range(n):
    for j in range(m):
        if (i >= 1) and (j >= 1):
            arr[i][j] += arr[i-1][j-1]

for i in range(q):
    y, x = map(int, input().split())
    print(arr[y-1][x-1])
