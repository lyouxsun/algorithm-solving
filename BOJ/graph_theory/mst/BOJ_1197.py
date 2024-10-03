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

# 1. 부모 노드를 찾는 함수
def get_parent(v):
    if cycle[v] != v:
        cycle[v] = get_parent(cycle[v])
    return cycle[v]

# 2. 두 부모 노드를 합치는 함수
def union(v1, v2):
    parent_v1 = get_parent(v1)
    parent_v2 = get_parent(v2)
    if parent_v1 > parent_v2:
        cycle[parent_v1] = parent_v2
    else:
        cycle[parent_v2] = parent_v1

def same_parent(v1, v2):
    parent_v1 = get_parent(v1)
    parent_v2 = get_parent(v2)
    if parent_v1 == parent_v2:
        return True
    else:
        return False

edge_cnt = 0
ans = 0

while q:
    if edge_cnt == v+1:
        break
    w, v1, v2 = heappop(q)
    if not same_parent(v1, v2):
        union(v1, v2)
        edge_cnt += 1
        ans += w

# print(cycle)
print(ans)