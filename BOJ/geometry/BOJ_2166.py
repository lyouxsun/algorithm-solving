# 신발끈공식 (2차원 도형 넒이) - 2166번 - 다각형의 면적
import sys, math
input = sys.stdin.readline
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
# print(points)

first = 0
for i in range(N-1):
    first += points[i][0] * points[i+1][1]
first += points[N-1][0] * points[0][1]

second = 0
for i in range(N-1):
    second += points[i][1] * points[i+1][0]
second += points[N-1][1] * points[0][0]

ans = abs(first-second) * 0.5
print(round(ans, 1))