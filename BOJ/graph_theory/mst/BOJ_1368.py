# MST - 1368번 - 물대기
import sys
from heapq import *
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
q = []
for i in range(1, n+1):
    heappush(q, (int(input()), i, 0))


for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n+1):
        if i != j:
            heappush(q, (line[j-1], i, j))

# 유니온파인드 ㄷㄱㅈ~
parent = [i for i in range(n+1)]


def get_parent(v):
    if v != parent[v]:
        parent[v] = get_parent(parent[v])
    return parent[v]

def union_parent(v1, v2):
    v1_parent = get_parent(v1)
    v2_parent = get_parent(v2)
    if v1_parent != v2_parent:
        if v1_parent > v2_parent:
            parent[v1_parent] = v2_parent
        else:
            parent[v2_parent] = v1_parent
        return True
    return False

## 최소 비용 트리 만들기
ans = 0
while q:
    w, s, e = heappop(q)
    if union_parent(s, e):
        ans += w

print(ans)
