# 그래프 - 1753번 - 최단경로
import sys, heapq

input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
graph = {i:[] for i in range(1, v+1)}

for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])
# print(graph)

q = []
result = [float('inf')] * (v + 1)
result[start] = 0
heapq.heappush(q, [0, start])       # 가중치, 도착노드

while q:
    res, now = heapq.heappop(q)
    for (weight, end) in graph[now]:
        # print('weight=', weight, ', end=', end)
        if result[end] > res + weight:
            result[end] = result[now] + weight
            heapq.heappush(q, [result[end], end])

# print(result)

for i in range(1, v + 1):
    if result[i] == float('inf'):
        print('INF')
    else:
        print(result[i])
