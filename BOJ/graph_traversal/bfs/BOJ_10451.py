# 그래프 탐색 - 10451 - 순열 사이클
import sys
from collections import deque
input = sys.stdin.readline

cycle = int(input())


def bfs(n):
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        next = graph[now]
        if visited[next] == 1:
            continue
        visited[next] = 1
        q.append(next)


for _ in range(cycle):
    num = int(input())
    graph = [0] * num
    visited = [0] * num

    input_graph = list(map(int, input().split()))
    for i in range(num):
        graph[i] = input_graph[i]-1

    cnt = 0
    for i in range(num):
        if visited[i] == 1:
            continue
        bfs(i)
        cnt += 1
    print(cnt)
