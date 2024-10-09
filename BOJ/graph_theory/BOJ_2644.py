# 그래프 이론(다익스트라) - 2644번 - 촌수계산
import sys
from heapq import *
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v = int(input())
start, end = map(int, input().split())
e = int(input())
edges = [[float('inf')]*(v+1) for _ in range(v+1)]
for i in range(e):
    v1, v2 = map(int, input().split())
    edges[v1][v2] = 1
    edges[v2][v1] = 1

result = [float('inf')] * (v+1)
q = []
result[start] = 0
heappush(q, (0, start))
while q:
    cost, now = heappop(q)
    for i in range(1, v+1):
        if edges[now][i] == 1:
            new_cost = cost + 1
            if result[i] > new_cost:
                result[i] = new_cost
                heappush(q, (new_cost, i))

# print(result)
if result[end] == float('inf'):
    print(-1)
else:
    print(result[end])