# 그래프 탐색 - 2583번 - 영역 구하기
## 1. 입력받기 -> 0으로 초기화 된 배열 만들기
## 2. 직사각형이 있는 부분은 1로 바꾸기
## 3. BFS -> 영역의 개수, 각 영역의 넓이 구하기  => 모두 출력

from collections import deque

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]
cnt = 0
ans = []
q = deque()
m, n, k = map(int, input().split())  # 세로 길이, 가로 길이, 직사각형 개수
arr = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    left_col, left_row, right_col, right_row = map(int, input().split())
    for i in range(left_row, right_row):
        for j in range(left_col, right_col):
            arr[i][j] = 1


def bfs():
    size = 1
    while q:
        row, col = q.popleft()
        arr[row][col] = 1
        for i in range(4):
            n_row = row + d_row[i]
            n_col = col + d_col[i]
            if (0 <= n_row < m) and (0 <= n_col < n):
                if arr[n_row][n_col] == 0:
                    arr[n_row][n_col] = 1
                    q.append([n_row, n_col])
                    size += 1
    return size


for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            q.append([i, j])
            ans.append(bfs())
            cnt += 1
ans.sort()

print(cnt)
for i in ans:
    print(i, end=' ')
