# 최단경로(다익스트라) - 1504번 - 특정한 최단 경로
from heapq import *
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = dict()
for i in range(1, n+1):
    d[i] = []

for _ in range(m):
    start, end, distance = map(int, input().split())
    d[start].append((end, distance))    # 딕셔너리는 list를 key로 사용할 수 없다!! -> tuple 사용하기!!
    d[end].append((start, distance))

# print(d)
end1, end2 = map(int, input().split())


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    ans_arr = [float('inf')] * (n + 1)
    ans_arr[start] = 0
    visited = [False] * (n + 1)
    while q:
        dist, now = heappop(q)
        if visited[now]:
            continue
        visited[now] = False
        arr = d[now]
        for (next, dist) in arr:
            if ans_arr[next]> ans_arr[now] + dist:
                ans_arr[next] = ans_arr[now] + dist
                if not visited[next]:
                    heappush(q, (ans_arr[next], next))
    return ans_arr

result = dijkstra(end1)    # end1 ~ end2 사이의 거리 구하기
ans = result[end2]
# print('시작 = end1 : ', result)
# print('end1 ~ end2 사이의 거리=', ans)

result1 = dijkstra(1)    # 1에서 시작해서 모든 노드 까지의 거리
result2 = dijkstra(n)    # n에서 시작해서 모든 노드 까지의 거리
# print('시작 = 1 : ', result1)
# print('시작 = n : ', result2)

sol1 = result1[end1] + result2[end2]
sol2 = result1[end2] + result2[end1]

if sol1 > sol2:
    ans += sol2
else:
    ans += sol1

if ans == float('inf'):
    print(-1)
else:
    print(ans)