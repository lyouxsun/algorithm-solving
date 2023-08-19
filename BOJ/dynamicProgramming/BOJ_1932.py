# 다이나믹 프로그래밍 - 1932번 - 정수 삼각형
## dp[j] = 삼각형 i번째 줄에 j번째 수를 반드시 포함한 경우의 합의 최댓값
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [[0 for i in range(N)]for i in range(N)]

for i in range(N):
    for j in range(i+1):
        dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    # print(dp)
print(max(dp[N-1]))