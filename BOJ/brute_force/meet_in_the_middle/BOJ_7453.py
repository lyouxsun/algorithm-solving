# 중간에서 만나기 - 7453번 - 합이 0인 네 정수
## A, B, C, D 배열이 n개의 크기로 세로로 나열되어 있다. -> A+B = -(C+D) 인 수를 찾자!
from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
a, b, c, d = [0] * n, [0] * n, [0] * n, [0] * n
for i in range(n):
    a[i], b[i], c[i], d[i] = map(int, input().split())
right = []
ans = 0
for i in range(n):
    for j in range(n):
        right.append(a[i] + b[j])

cnt = Counter(right)
for i in range(n):
    for j in range(n):
        ans += cnt[-c[i] - d[j]]
print(ans)
