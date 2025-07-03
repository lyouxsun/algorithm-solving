# MST - 14950번 - 정복자
import sys
from heapq import *
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e, t = map(int, input().split())
q = []
for i in range(e):
    s, e, c = map(int, input().split())
    heappush(q, (c, s-1, e-1))

cycle = [i for i in range(v)]
def get_parent(v):
    if cycle[v] != v:
        cycle[v] = get_parent(cycle[v])
    return cycle[v]

def union_parent(v1, v2):
    v1_parent = get_parent(v1)
    v2_parent = get_parent(v2)
    if v1_parent != v2_parent:
        if v1_parent > v2_parent:
            cycle[v1_parent] = v2_parent
        else:
            cycle[v2_parent] = v1_parent
        return True
    return False

ans = 0
cnt = 0
edge_cnt = 0
while q:
    c, s, e = heappop(q)
    if union_parent(s, e):
        ans += (c + t * cnt)
        cnt += 1
        edge_cnt += 1
    if edge_cnt == v-1:
        break

print(ans)