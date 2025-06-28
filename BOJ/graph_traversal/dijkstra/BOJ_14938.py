# 다익스트라 - 14938번 - 서강그라운드
import sys
from heapq import *
input = sys.stdin.readline
INF = float("inf")

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
## 인접 리스트X, 인접 행렬 형태로 입력받기
for _ in range(R):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))
# for i in range(1, N+1):
#     print(i, '=', graph[i])
# print()

def dijkstra(s):
    # 1. 초기화 작업
    dp = [INF for _ in range(N + 1)]
    dp[s] = 0
    q = []
    heappush(q, (0, s))

    # 2. s 에서 모든 노드까지의 최단경로 구하기 (dp 갱신하기)
    while q:  # 힙이 비면 종료
        dist, now = heappop(q)      # dist : s부터 now 까지의 최단경로
        for (end, cost) in graph[now]:      # cost : now부터 end 까지의 간선 비용
            if dp[end] > dist + cost:
                dp[end] = dist + cost
                heappush(q, (dp[end], end))
    return dp


# s 에서 모든 노드까지의 거리 구하기
ans = 0
for start in range(1, N+1):
    distance = dijkstra(start)

    # 3. 방문 가능한 노드의 아이템 개수만 더하기
    result = 0
    for i in range(1, N + 1):
        if distance[i] <= M:
            result += items[i - 1]
    ans = max(result, ans)
    # print(s, '에서 시작했을 때 모든 모드까지의 최단경로=', dp)
    # print(s, '부터 시작했을 때 얻을 수 있는 아이템 개수 =', result)
print(ans)