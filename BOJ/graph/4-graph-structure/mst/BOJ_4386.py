# MST - 4386번 - 별자리 만들기
## 둘 사이의 거리를 구하는 함수 따로 정의하기
import sys, math
from itertools import combinations
from heapq import *
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
coord = [[0, 0] for _ in range(n+1)]
for i in range(1, n+1):
    coord[i] = list(map(float, input().split()))

comb = [i for i in range(1, n+1)]
two_stars = combinations(comb, 2)

def distance(a, b):
    x1, y1 = coord[a]
    x2, y2 = coord[b]
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)

q =[]
for (a, b) in two_stars:
    cost = distance(a, b)
    heappush(q, (cost, a, b))


## 유니온 파인드
cycle = [i for i in range(0, n+1)]

def get_parent(a):
    if a != cycle[a]:
        cycle[a] = get_parent(cycle[a])        # 경로 압축!!!!
    return cycle[a]

def same_parent(a, b):
    cycle[a] = get_parent(a)
    cycle[b] = get_parent(b)
    if cycle[a] == cycle[b]:
        return True
    return False

def union_parent(a, b):
    a_parent = get_parent(a)
    b_parent = get_parent(b)

    if a_parent > b_parent:
        cycle[a_parent] = b_parent
    else:
        cycle[b_parent] = a_parent

ans = 0.0
edge_cnt = 0
while q:
    w, v1, v2 = heappop(q)
    if not same_parent(v1, v2):
        union_parent(v1, v2)
        ans += w
        edge_cnt += 1
    if edge_cnt == n-1:
        break

print(ans)