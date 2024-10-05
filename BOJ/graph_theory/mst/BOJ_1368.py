# MST - 1368번 - 물대기
import sys
from heapq import *
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
q = []
for i in range(n):
    well = int(input())
    heappush(q, (well, i, -1))


for i in range(n):
    line = list(map(int, input().split()))
    for j in range(i + 1, n):
        heappush(q, (line[j], i, j))

# 유니온파인드 ㄷㄱㅈ~
cycle = [i for i in range(n)]


def get_parent(v):
    if v != cycle[v]:
        cycle[v] = get_parent(cycle[v])
    return cycle[v]

def same_parent(v1, v2):
    return get_parent(v1) == get_parent(v2)


def union_parent(v1, v2):
    v1_parent = get_parent(v1)
    v2_parent = get_parent(v2)
    if v1_parent > v2_parent:
        cycle[v1_parent] = v2_parent
    else:
        cycle[v2_parent] = v1_parent



## 최소 비용 트리 만들기
well_connected = [False] * n  # 우물이 판 논을 추적하기 위한 배열

edge_cnt, ans = 0, 0
well = False
while q:
    w, s, e = heappop(q)
    if e == -1:      # 우물 추가
        if not well_connected[s] or not well:      # 아직 엣지를 연결하지 않은 논!
            ans += w
            edge_cnt += 1
            union_parent(s, s)
            well_connected[s] = True
            well = True

    else:           # 엣지 추가
        if not same_parent(s, e):
            union_parent(s, e)
            ans += w
            edge_cnt += 1
            well_connected[s] = well_connected[e] = True

    if edge_cnt == n:
        break
print(ans)
