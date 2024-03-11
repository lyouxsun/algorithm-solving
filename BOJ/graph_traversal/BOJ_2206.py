# 2206번 - 그래프 탐색 - 벽 부수고 이동하기
## sol 1. 존재하는 모든 벽을 하나씩 없애면서 그 때의 최단경로 계산 -> 그 중 가장 최소값 찾기 (경로 없으면 -1) => n*m*(벽 개수) 시간복잡도로 무조건 시간초과 발생
## sol 2. 방문 배열을 3차원으로 만들기 (높이 0 : 벽 부순 적 없음. 높이 1 : 벽 이미 부숨) => 정답!

from collections import deque
import sys

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append([0, 0, 0])  # 순서대로 행/열/부순벽개수
    while q:
        y, x, break_cnt = q.popleft()
        if y == n - 1 and x == m - 1:
            return visited[y][x][break_cnt]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < n) and (0 <= nx < m):
                if (arr[ny][nx] == 1) and (break_cnt == 0):
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    q.append([ny, nx, 1])
                if (arr[ny][nx] == 0) and (visited[ny][nx][break_cnt] == 0):
                    visited[ny][nx][break_cnt] = visited[y][x][break_cnt] + 1
                    q.append([ny, nx, break_cnt])
    return -1


n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
result = bfs()
if result == -1:
    print(result)
else:
    print(result + 1)
