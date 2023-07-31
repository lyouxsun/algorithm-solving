# 그리디 알고리즘 - 10775번 - 공항
import sys
input = sys.stdin.readline
gate = int(input())
plane = int(input())
arr = []
result = [0]*(gate+1)
cnt = 0

for _ in range(plane):
    tmp = int(input())
    for i in range(tmp, -1, -1):
        if i == 0:
            break
        if result[i] == 0:
            result[i] = 1
            cnt += 1
            break
    if i == 0:
        break
print(cnt)