# 브루트 포스 - 16988번 - Baaaaaaaaaduk2 (Easy)
## 그룹이 빈틈없이 에워싸였다 == 그 그룹 내에 빈칸과 인접해있는 돌이 하나도 없다
## 돌을 둘 수 있는 모든 경우의 수 생각하기 => 400C2 = 80000정도
## 각 경우마다 죽인 2의 개수를 세는 복잡도 =>
import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
baduk = [0] * n
for i in range(n):
    baduk[i] = list(map(int, input().split()))
ans = 0


## 2. 돌 2개 놓은 후 죽은 2의 개수 구하는 부분
## 2가 빈틈없이, 1로만 둘러싸여있는 부분 찾아서, -> 그 안에 있는 2의 개수를 구하는 함수
## 주변에 1만 있어야됨, 0 있으면 안됨,
def cnt(baduk_arr):
    arr = copy.deepcopy(baduk_arr)
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q = []
                dead = True
                q.append([i, j])
                arr[i][j] = -1
                tmp = 1
                while len(q) > 0:
                    y, x = q.pop(0)
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if (0 <= ny < n) and (0 <= nx < m):
                            if arr[ny][nx] == 0:
                                dead = False
                            elif arr[ny][nx] == 2:
                                q.append([ny, nx])
                                arr[ny][nx] = -1
                                tmp += 1

                if dead:
                    result += tmp
    return result


## 1. 돌 놓는 부분
for i in range(n):
    for j in range(m):
        if baduk[i][j] == 0:
            baduk[i][j] = 1
            for k in range(n):
                for l in range(m):
                    if baduk[k][l] == 0:
                        baduk[k][l] = 1
                        ans = max(ans, cnt(baduk))
                        baduk[k][l] = 0
            baduk[i][j] = 0
print(ans)
