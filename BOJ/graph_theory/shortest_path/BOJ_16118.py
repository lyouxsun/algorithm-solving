# 다익스트라 - 16118번 - 달빛 여우
# 여우의 최소비용과 늑대의 최소비용을 각각 구한 뒤, 그 중 여우가 더 빨리 도착할 수 있는 노드의 개수를 구한다.
import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())
roads = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    roads[s].append((e, c))
    roads[e].append((s, c))

## 1. 달빛 여우의 최단 거리 구하기
fox = [float('inf')] * (n + 1)
fox[1] = 0
q = []
heapq.heappush(q, [0, 1])  # 현재 노드, 누적 비용
while q:
    cost, now = heapq.heappop(q)
    if cost > fox[now]:
        continue
    for (next, next_cost) in roads[now]:
        new_cost = fox[now] + next_cost
        if fox[next] > new_cost:
            fox[next] = new_cost
            heapq.heappush(q, [new_cost, next])
# print(fox)

## 2. 달빛 늑대의 최단 거리 구하기
wolf_q = [[float('inf')] * (n + 1) for _ in range(2)]
wolf_q[0][1] = 0
visited = [[0] * (n + 1) for _ in range(2)]
q = []
heapq.heappush(q, [0, 1, 1])  # 현재 노드, 누적 비용

while q:
    cost, now, fast = heapq.heappop(q)  # fast=1 : 비용*0.5 더하기, 0 : 비용*2 더하기
    # print('[pop] now=%d, cost=%f, fast=%d' % (now, cost, fast))
    if cost > wolf_q[1 - fast][now]:
        continue
    speed = 0.5 if fast else 2

    for (next, next_cost) in roads[now]:
        new_cost = wolf_q[1 - fast][now] + next_cost * speed
        if wolf_q[fast][next] > new_cost:
            wolf_q[fast][next] = new_cost
            # print('now=%d to i=%d, dist=%f, fast=%d' % (now, i, wolf_q[fast][i], fast))
            heapq.heappush(q, [new_cost, next, 1 - fast])
wolf = [min(wolf_q[0][i], wolf_q[1][i]) for i in range(n + 1)]
# print(wolf_q)
# print(wolf)
## 3. 비교
ans = 0
for i in range(1, n + 1):
    if fox[i] < wolf[i]:
        ans += 1
print(ans)

# 4 4
# 1 2 1
# 2 3 10
# 2 4 1
# 4 1 1

# 5 5
# 1 2 1
# 2 3 1
# 1 3 1
# 1 4 1
# 4 5 10000
# 답 : 0
