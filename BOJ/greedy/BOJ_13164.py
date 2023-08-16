# 그리디 알고리즘 - 13164번 - 행복 유치원
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
dif = []
for i in range(N-1):
    dif.append(arr[i+1]-arr[i])
dif.sort()
total = 0
for i in range(N-K):
    total += dif[i]
print(total)