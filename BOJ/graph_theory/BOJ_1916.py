# 그래프 이론 - 1916번 - 최소비용 구하기
## 비용은 딕셔너리로 구하고, 다익스트라는 큐?힙?으로 구현
import sys, heapq
input = sys.stdin.readline

v = int(input())
bus_num = int(input())
city = [[float('inf')]*(v+1) for _ in range(v+1)]
for _ in range(bus_num):
    s, e, cost = map(int, input().split())
    city[s][e] = min(city[s][e], cost)
start, end = map(int, input().split())

q = []
result = [float('inf')] * (v + 1)
result[start] = 0
heapq.heappush(q, [0, start])       # 가중치, 도착노드

while q:
    res, now = heapq.heappop(q)
    for i in range(v+1):
        if result[i] > res + city[now][i]:
            result[i] = result[now] + city[now][i]
            heapq.heappush(q, [result[i], i])

# print(result)
print(result[end])
# 2
# 2
# 1 2 0
# 1 2 10
# 1 2
# 답 : 0
