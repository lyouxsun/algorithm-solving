# 그래프 이론 - 1012번 - 유기농 배추
import sys
input = sys.stdin.readline
def bfs(M, N, arr):
    cnt = 0
    queueArr = []
    for x in range(M):
        for y in range(N):
            if arr[y][x] == 1:
                cnt += 1
                queueArr.append([y, x])
                while len(queueArr) != 0:
                    b, a = queueArr.pop()
                    arr[b][a] = 0

                    if b!= N-1:
                        if arr[b+1][a] == 1:
                            queueArr.append([b+1, a])
                    if a!= M-1:
                        if arr[b][a+1] == 1:
                            queueArr.append([b, a+1])
                    if b!=0:
                        if arr[b-1][a] == 1:
                            queueArr.append([b-1, a])
                    if a!=0:
                        if arr[b][a-1] == 1:
                            queueArr.append([b, a-1])
    print(cnt)


cycle = int(input())
for i in range(cycle):
    # 그래프 만들기
    M, N, K = map(int, input().split())
    arr = [[0 for a in range(M)] for b in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    # 그래프 탐색하기
    bfs(M, N, arr)


