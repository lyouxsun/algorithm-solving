# 위상정렬 - 1766번 - 문제집
import heapq
import sys

n, m = map(int, input().split())
d = dict()
for i in range(n):
    d[i+1] = [i+1, 0, []]

for i in range(m):
    a, b = map(int, input().split())
    d[b][1] += 1
    d[a][2].append(b)

h = []
for i in range(1, n+1):
    if d[i][1] == 0:
        heapq.heappush(h, d[i][0])

# print(h)
# print(d)


result = []
while h:
    now = heapq.heappop(h)
    result.append(now)
    for i in d[now][2]:
        d[i][1] -= 1
        # print('i=', i, ', d[i][1] =', d[i][1])
        if d[i][1] == 0:
            heapq.heappush(h, d[i][0])
    # print(d)
for i in result:
    print(i, end=' ')