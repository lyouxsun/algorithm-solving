# 다이나믹 프로그래밍 - 11053번 - 가장 긴 증가하는 부분 수열
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

# 1 5 3 6 4 9 9 9 9 9 5 6 7 8 9
# i번째 수 까지의 부분증가수열 개수의 최댓값 (i번째 수를 반드시 포함해야함)
# 1 2 2 3 3 4 4 4 4 4 4 5 6 7 8