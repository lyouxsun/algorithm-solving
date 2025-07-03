# DP - 1965번 - 상자넣기
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
tmp = 0
dp = [0 for i in range(N)]
dp[0] = 1
for i in range(N):
    for j in range(i):
        if arr[j]<arr[i]:
            tmp = dp[j]+1
        else:
            tmp = 1
        dp[i] = max(dp[i], tmp)
# print(dp)
print(max(dp))