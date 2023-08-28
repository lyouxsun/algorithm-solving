# 다이나믹 프로그래밍 - 14501번 - 퇴사
## 아이디어 : dp[i] = i번째 날~퇴사일 까지 벌 수 있는 최대 수입
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)
dp = [0 for i in range(N+1)]
answer = 0
for i in range(N-1, -1, -1):
    if i+arr[i][0]<=N:
        dp[i] = max(dp[i+arr[i][0]]+arr[i][1], dp[i+1])
    else:
        dp[i] = dp[i + 1]
    # print(i)
    # print(dp[i])
print(dp[0])