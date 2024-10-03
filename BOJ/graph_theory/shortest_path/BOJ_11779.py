# 다익스트라 - 11779번 - 최소비용 구하기2
from heapq import *
import sys
input = sys.stdin.readline

v = int(input())
e = int(input())
bus = [[] for _ in range(v + 1)]
for _ in range(e):
    s, e, w = map(int, input().split())
    bus[s].append([e, w])
start, end = map(int, input().split())

result = [float('inf')] * (v + 1)
# path = [[] for _ in range(v + 1)]
path = [0]*(v+1)
q = []
result[start] = 0
heappush(q, [0, start])

while q:
    cost, now = heappop(q)
    if result[now] < cost:      # 이미 처리된 노드 건너뛰기
        continue
    for [next, weight] in bus[now]:
        new_cost = result[now] + weight
        # if result[next] == new_cost:
        #     path[next].append(now)
        if result[next] > new_cost:
            result[next] = new_cost
            # path[next].clear()
            path[next] = now
            heappush(q, [new_cost, next])

print(result[end])
now = end
path_ans = []
path_ans.append(end)
while True:
    if path[now] == 0:
        break
    # if len(path[now]) == 0:
    #     break
    before = path[now]
    path_ans.append(before)
    now = before
length = len(path_ans)
print(length)
# path_ans.reverse()
# print(' '.join(map(str, path_ans)))
for i in range(length-1, -1, -1):
    print(path_ans[i], end = ' ')
