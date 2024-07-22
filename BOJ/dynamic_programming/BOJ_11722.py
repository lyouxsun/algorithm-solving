# 동적 프로그래밍 - 11722번 - 가장 긴 감소하는 부분 수열

N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(0, i):
        if arr[i] < arr[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))