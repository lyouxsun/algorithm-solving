# 다익스트라 - 1167번 - 트리의 지름
import sys
from heapq import *
input = sys.stdin.readline
INF = float('inf')

V = int(input())
graph = [[] for _ in range(V+1)]
for i in range(V):
    nums = list(map(int, input().split()))
    start = nums[0]
    for i in range(len(nums)//2):
        if nums[2 * i + 1] == -1:
            break
        dst, cost = nums[2 * i + 1], nums[2 * i + 2]
        graph[start].append((dst, cost))

# for i in range(V):
#     print(graph[i])

def dijkstra(s):
    dp = [INF] * (V+1)
    dp[s] = 0
    q = []
    heappush(q, (0, s))
    while q:
        dist, now = heappop(q)
        ### 추가
        if dist > dp[now]:
            continue


        for next, cost in graph[now]:
            # if dp[next] > dist + cost:
            if dp[next] > dp[now] + cost:
                dp[next] = dp[now] + cost
                # dp[next] = dist + cost
                heappush(q, (dp[next], next))
            # print('now=', now, ', next=', next, ', 둘 사이의 cost=', cost)
    # print(dp)
    return dp

dp = dijkstra(start)
farthest = dp.index(max(dp[1:]))  # INF 제외하고 가장 먼 노드
dp = dijkstra(farthest)
print(max(dp[1:]))

# ans = -1
# for start in range(1, V+1):
#     dp = dijkstra(start)
#     ans = max(ans, max(dp[i] for i in range(1, V+1) if dp[i] != INF))
# print(ans)