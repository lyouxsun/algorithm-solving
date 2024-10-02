# 다익스트라 - 1197번 - 최소 스패닝 트리
import sys
from heapq import *
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
q = []

for _ in range(e):
    v1, v2, weight = map(int, input().split())
    heappush(q, (weight, v1, v2))

cycle = [i for i in range(v+1)]
# print(cycle)

def find_parent(v):
    if cycle[v] != v:
        cycle[v] = find_parent(cycle[v])
    return cycle[v]

def union(v1, v2):
    parent_v1 = find_parent(v1)
    parent_v2 = find_parent(v2)
    if parent_v1 > parent_v2:
        cycle[parent_v1] = parent_v2
    else:
        cycle[parent_v2] = parent_v1

edge_cnt = 0
ans = 0

while q:
    if edge_cnt == v+1:
        break
    w, v1, v2 = heappop(q)
    if find_parent(v1) != find_parent(v2):
        union(v1, v2)
        edge_cnt += 1
        ans += w

# print(cycle)
print(ans)