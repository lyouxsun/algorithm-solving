# 누적합 - 32715번 - 십자 찾기
import sys
input = sys.stdin.readline

arr = []

r, c = map(int, input().split())
k = int(input())
garo = [[0] * (c+1) for _ in range(r+1)]
sero = [[0] * (c+1) for _ in range(r+1)]
for i in range(r):
    line = list(map(int, input().split()))
    arr.append(line)

# 각 행의 누적합 : garo
for i in range(1, r+1):
    for j in range(1, c+1):
        if i == 1 and j == 1:
            garo[i][j] = arr[i-1][j-1]
            sero[i][j] = arr[i-1][j-1]
        elif i == 1:
            garo[i][j] = garo[i][j-1] + arr[i-1][j-1]
            sero[i][j] = arr[i-1][j-1]
        elif j == 1:
            garo[i][j] = arr[i-1][j-1]
            sero[i][j] = sero[i-1][j] + arr[i-1][j-1]
        else:
            garo[i][j] = garo[i][j-1] + arr[i-1][j-1]
            sero[i][j] = sero[i-1][j] + arr[i-1][j-1]


# print('sero')
# for i in range(r):
#     print(sero[i])
# print()
# print('garo')
# for i in range(r):
#     print(garo[i])

# x, y : 십자가 중심의 좌표
ans = 0
for y in range(k-1, r-k):
    for x in range(k-1, c-k):
        if arr[y][x] == 1:
            # print('y=', y, ', x=', x)
            if ((garo[y+1][x+k+1] - garo[y+1][x-k] == 2*k+1) and
                    (sero[y+k+1][x+1] - sero[y-k][x+1] == 2*k+1)):
                # print('*** y=', y, ', x=', x)

                ans += 1

print(ans)
