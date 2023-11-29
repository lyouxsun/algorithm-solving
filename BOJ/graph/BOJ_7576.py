# 그래프 이론 - 토마토 - 7576번
import sys
input = sys.stdin.readline
graph = []
inputArr = []
M, N = map(int, input().split())
# arr에 데이터 넣기
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            inputArr.append((i, j))        # i:몇행 j:몇열
    graph.append(row)

cnt = 0
change = False

while len(inputArr) != 0:
    cnt += 1
    # print("\n", cnt)
    # print(inputArr)
    output = inputArr[:]
    inputArr.clear()
    while len(output) != 0:
        y, x = output.pop()
        change = False
        if x != 0:  # 왼
            if graph[y][x - 1] == 0:
                graph[y][x - 1] = 1
                inputArr.append((y, x - 1))
                change = True
        if x != M-1:    # 오
            if graph[y][x + 1] == 0:
                graph[y][x + 1] = 1
                inputArr.append((y, x + 1))
                change = True
        if y != 0:      # 위
            if graph[y - 1][x] == 0:
                graph[y - 1][x] = 1
                inputArr.append((y - 1, x))
                change = True
        if y != N-1:        # 아래
            if graph[y + 1][x] == 0:
                graph[y + 1][x] = 1
                inputArr.append((y + 1, x))
                change = True
if change == False:
    cnt-=1
# print(graph)

success = True
for row in graph:
    if 0 in row:
        success = False
        break
if success == True:
    print(cnt)
else:
    print("-1")

# 0 0 0 0 0 0   ➡️여기가 y == 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1   ➡️여기가 y == N-1
#⬇️         ⬇️
# 여         여
# 기         기
# 가         가
# x==0      x==M-1