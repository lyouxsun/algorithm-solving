# 다익스트라 - 2307번 - 도로검문
from heapq import *
import sys
input = sys.stdin.readline


# 처음 최단경로를 찾을 때에만 사용 (경로 탐색을 위해서 배열을 하나 더 사용함)
def dijkstra():
    result = [float('inf')] * (v + 1)
    way = [[] for _ in range(v + 1)]

    result[1] = 0
    q = []
    heappush(q, (0, 1))  # 누적 비용, 지금 노드
    # 1. 검문이 없을 때의 최소 시간 구하기
    while q:
        cost, now = heappop(q)
        if cost > result[now]:
            continue
        for next, weight in edges[now]:
            new_cost = cost + weight
            if result[next] == new_cost:
                way[next].append(now)
            if result[next] > new_cost:
                result[next] = new_cost
                way[next] = [now]
                heappush(q, (new_cost, next))
    return result, way


# 도로검문 시 사용 (경로 탐색할 필요가 없는 경우)
def modified_dijkstra(blocked_road):
    result = [float('inf')] * (v + 1)
    result[1] = 0
    q = []
    heappush(q, (0, 1))  # 누적 비용, 지금 노드

    while q:
        cost, now = heappop(q)
        if cost > result[now]:
            continue
        for next, weight in edges[now]:
            if (now, next) in blocked_road or (next, now) in blocked_road:      # 검문을 시행하는 도로는 건너뜀
                continue
            new_cost = cost + weight
            if result[next] > new_cost:
                result[next] = new_cost
                heappush(q, (new_cost, next))
    return result[v]


v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]  # 인접 리스트로 그래프 가중치를 저장
for i in range(e):
    a, b, w = map(int, input().split())
    edges[a].append((b, w))
    edges[b].append((a, w))

# 1. 도로검문이 없을 때 최단경로를 구한다.  (min_cost)
result, path = dijkstra()
min_cost = result[v]

# 2. 최단경로가 되는 모든 경로를 찾아서 check 집합에 저장한다.
# (path[end] 부터 path[start]까지 역추적하며 경로를 찾아낸다)
tmp = [v]
check = set()
while tmp:
    now = tmp.pop()
    for before in path[now]:
        check.add((now, before))
        tmp.append(before)
# print(check)

# 3. check 배열에 저장된 모든 도로를 하나씩 막으며 지연시간의 최댓값을 구한다.
max_cost = 0
for (now, before) in check:
    blocked_road = {(now, before)}
    delay = modified_dijkstra(blocked_road)
    if max_cost == float('inf'):
        break
    max_cost = max(max_cost, delay)

if max_cost == float('inf'):
    print(-1)
else:
    print(max_cost - min_cost)


