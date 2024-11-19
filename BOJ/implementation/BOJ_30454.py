# 구현 - 30454번 - 얼룩말을 찾아라!
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
ans, num = 0, 0
for i in range(n):
    zebra = list(input().strip())
    cnt = 0
    if zebra[0] == '1':
        cnt += 1
    for j in range(1, l):
        if zebra[j] == '1' and zebra[j-1] == '0':
            cnt += 1

    if cnt > ans:
        ans = cnt
        num = 1
    elif cnt == ans:
        num += 1

print(ans, num)