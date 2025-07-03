# MST - 1647번 - 도시 분할 계획
## 마을을 두개로 분리한다고 했으니까 MST를 수행하고, 다 끝난 후에는 마지막 간선만 빼주면 될듯

import sys
from heapq import *
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
q = []
for _ in range(e):
    s, e, w = map(int, input().split())
    heappush(q, (w, s, e))

### 유니온파인드~
cycle = [i for i in range(v+1)]
def get_parent(v):
    if v == cycle[v]:
        return v
    return get_parent(cycle[v])

def same_parent(v1, v2):
    cycle[v1] = get_parent(v1)
    cycle[v2] = get_parent(v2)
    if cycle[v1] == cycle[v2]:
        return True
    return False

def union_parent(v1, v2):
    if not same_parent(v1, v2):
        v1_p = cycle[v1]
        v2_p = cycle[v2]
        if v1_p > v2_p:
            cycle[v1_p] = v2_p
        else:
            cycle[v2_p] = v1_p
        return True
    else:
        return False
last, ans, edge_cnt = 0, 0, 0

while q:
    if edge_cnt >= v-2:      # 마을이 2개밖에 없는 경우, 연결할 필요가 없다.
        break
    w, s, e = heappop(q)
    if union_parent(s, e):
        edge_cnt += 1
        ans += w
        last = w

print(ans)