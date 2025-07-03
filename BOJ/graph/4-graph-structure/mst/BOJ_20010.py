# MST+BFS - 20010번 - 악덕 영주 혜유
# 1. MST를 구하기
import sys
from heapq import *
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
q = []
for i in range(e):
    a, b, c = map(int, input().split())
    heappush(q, (c, a, b))

parent = [i for i in range(v)]
def find_parent(v):
    if parent[v]!=v:
        parent[v] = find_parent(parent[v])
    return parent[v]

def union_parent(v1, v2):
    v1_parent = find_parent(v1)
    v2_parent = find_parent(v2)
    if v1_parent != v2_parent:
        if v1_parent > v2_parent:
            parent[v1_parent] = v2_parent
        else:
            parent[v2_parent] = v1_parent
        return True
    return False

ans = 0
graph = [[] for _ in range(v)]
while q:
    c, a, b = heappop(q)
    if union_parent(a, b):
        ans += c
        graph[a].append([b, c])
        graph[b].append([a, c])
print(ans)

## 2. MST에서 두 마을 간 최고 비용 구하기 - dfs
def dfs(u, p):
    result = (0, u) # 현재 제일 먼 정점까지의 거리와 그 정점
    for v, w in graph[u]:
        if v == p:
            continue
        dist, far = dfs(v, u)
        result = max(result, (dist + w, far))
    return result

_, far = dfs(0, -1)
print(dfs(far, -1)[0])