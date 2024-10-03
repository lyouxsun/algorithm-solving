# MST - 1922번 - 네트워크 연결
from heapq import *
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v = int(input())
e = int(input())
q = []
for _ in range(e):
    s, e, w = map(int, input().split())
    heappush(q, (w, s, e))      # 비용을 오름차순으로 나열하도록 힙에 저장

# 유니온 파인드를 위한 3개의 함수 구현
cycle = [i for i in range(v+1)]
## 1. 부모 찾는 함수
def get_parent(v):
    if v == cycle[v]:
        return v
    cycle[v] = get_parent(cycle[v])
    return cycle[v]

def same_parent(v1, v2):
    cycle[v1] = get_parent(v1)
    cycle[v2] = get_parent(v2)
    if cycle[v1] == cycle[v2]:
        return True
    return False

def union_parent(v1, v2):
    v1_p = cycle[v1]
    v2_p = cycle[v2]
    if v1_p > v2_p:
        cycle[v1_p] = v2_p      # 나의 cycle 테이블이 아닌, 부모의 cycle 테이블을 갱신해야 한다.
    else:
        cycle[v2_p] = v1_p


edge_cnt = 0
ans = 0
while q:
    if edge_cnt == v - 1:
        break
    w, s, e = heappop(q)
    if not same_parent(s, e):
        union_parent(s, e)
        edge_cnt += 1
        ans += w
        # print(s, e)
        # print(cycle)
print(ans)