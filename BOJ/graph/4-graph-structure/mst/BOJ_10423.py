# MST - 10423번 - 전기가 부족해
import sys
from heapq import *

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

v, e, e_num = map(int, input().split())
electric = list(map(int, input().split()))
edges = []
q = []
for i in range(e):
    s, e, c = map(int, input().split())
    heappush(q, (c, s, e))

## 발전소라면 parent가 0이다 -> 발전소를 항상 parent로 만들기 위해서!!!
cycle = [i for i in range(v+1)]
for i in electric:
    cycle[i] = 0
# print(cycle)


## 유니온 파인드
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


edge_cnt = 0
ans = 0
while q:
    c, s, e = heappop(q)
    if union_parent(s, e):
        ans += c
        edge_cnt += 1
    if edge_cnt == v-e_num:
        break
print(ans)
