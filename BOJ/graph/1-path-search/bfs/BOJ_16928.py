# BFS - 16928번 - 뱀과 사다리 게임
## 보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다. => 그래프 형태
## 도착한 칸이 사다리나 뱀이면 자동 이동 => 간선이 휘어지기도 함 (순차X, 점프/후퇴도 있음)
## 주사위를 던지는 건 항상 동일한 비용이 든다 => 가중치가 모두 1

import sys
from collections import deque
input = sys.stdin.readline

# 1. 입력받기
n, m = map(int, input().split())

# 2. 게임판 배열 초기화
board = [i for i in range(101)]
visited = [False for _ in range(101)]

for _ in range(n):
    start, end = list(map(int, input().split()))
    board[start] = end
for _ in range(m):
    start, end = list(map(int, input().split()))
    board[start] = end

# 3. bfs : queue 순회하며 모든 칸 탐색하기
q = deque()
q.append((1, 0))  # 시작점, 시작점까지의 이동횟수
visited[1] = True

while deque:
    now, cnt = q.popleft()
    # print('now=', now, ', cnt=', cnt)
    if now == 100:
        print(cnt)
        break
    for i in range(1, 7):
        if 100 < now + i:
            continue
        next = now + i
        if not visited[board[next]]:
            visited[board[next]] = True
            # 아무것도 없는 경우, 사다리 있음, 뱀 있음 모두 동일하게 처리
            q.append((board[next], cnt + 1))
