# 다익스트라 - 1389번 - 케빈 베이컨의 6단계 법칙
from heapq import *
v, e = map(int, input().split())
graph = [[0]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dijkstra(start):
    result = [float('inf')] * (v + 1)
    result[0] = 0
    result[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        cost, now = heappop(q)
        for next in range(1, v+1):
            if graph[now][next] == 1:
                if result[next] > cost+1:
                    result[next] = cost+1
                    heappush(q, (result[next], next))
    # print('result =', result)

    return sum(result)


answer = [float('inf')] * (v+1)
for start in range(1, v+1):     # 하나씩 시작 노드로 삼아서 탐색하기
    answer[start] = dijkstra(start)
# print('answer =', answer)
min_ = float('inf')
ans = 0
for i in range(1, v+1):
    if answer[i] < min_:
        ans = i
        min_ = answer[i]

print(ans)