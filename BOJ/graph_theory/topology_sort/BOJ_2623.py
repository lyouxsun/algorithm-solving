import sys
from heapq import *

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0, []] for i in range(n + 1)]

for j in range(m):
    l = list(map(int, input().split()))
    length = l.pop(0)
    now, next = l[0], 0
    for i in range(length - 1):
        next = l[i + 1]
        arr[now][1].append(next)
        arr[next][0] += 1
        now = next

q = []
ans = []
for i in range(1, n + 1):
    if arr[i][0] == 0:
        heappush(q, i)

cnt = 0
while q:
    now = heappop(q)
    cnt += 1
    ans.append(now)

    for next in arr[now][1]:
        arr[next][0] -= 1
        if arr[next][0] == 0:
            heappush(q, next)

if cnt != n:
    print(0)
else:
    for i in ans:
        print(i)
