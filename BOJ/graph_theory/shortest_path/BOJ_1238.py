# 다익스트라 - 1238번 - 파티
import sys
from heapq import *
input = sys.stdin.readline

n, m, x = map(int, input().split())
roads = [[] for _ in range(m+1)]
for i in range(m):
    s, e, c = map(int, input().split())
    roads[s].append((c, e))
# print(roads)

def to_party(start, end):
    global n
    result = [float('inf')] * (n + 1)
    result[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        cost, now = heappop(q)
        for (weight, next) in roads[now]:
            # if cost < weight:
            #     continue
            new_cost = cost + weight
            if result[next] > new_cost:
                result[next] = new_cost
                if next != x:
                    heappush(q, (new_cost, next))
    return result[end]

# x에서 i 로 가는 비용
def from_party(start):
    global n
    result = [float('inf')] * (n + 1)
    result[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        cost, now = heappop(q)
        for (weight, next) in roads[now]:
            new_cost = cost + weight
            if result[next] > new_cost:
                result[next] = new_cost
                if next != x:
                    heappush(q, (new_cost, next))
    return result


toParty = [0] * (n+1)
for i in range(1, n+1):
    if i == x:
        continue
    toParty[i] = to_party(i, x)
fromParty = from_party(x)
result = [fromParty[i]+toParty[i] for i in range(n+1)]

print(max(result[1:n+1]))