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

    if i == 0:
        for j in range(c):
            sero[i+1][j+1] = line[j]
    else:
        for j in range(c):
            sero[i+1][j+1] = sero[i][j+1] + line[j]

    garo[i+1][1] = line[0]
    for j in range(c):
        garo[i+1][j+1] = garo[i+1][j] + line[j]

# for i in range(r+1):
#     print(sero[i])
# print()
# for i in range(r):
#     print(garo[i])

if k == 0:
    ans = 0
    for i in range(r):
        ans += garo[i][-1]
    print(ans)
    exit()

# x, y : 십자가 중심의 좌표
ans = 0
for y in range(k, r-k):
    for x in range(k, c-k):

        if arr[y][x] == 1:
            # print('y=', y, ', x=', x)

            if (garo[y+1][x+k+1] - garo[y+1][x-k] == 2*k+1) and (sero[y+k+1][x+1] - sero[y-k][x+1] == 2*k+1):
                # print('*** y=', y, ', x=', x)

                ans += 1

print(ans)
