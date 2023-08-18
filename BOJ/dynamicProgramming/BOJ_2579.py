# 다이나믹 프로그래밍 - 2579번 - 계단 오르기
## 배열로 입력을 받기, 붙어있는거 : 2개까지만, 비어있는거 1개씩만 가능
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
# dp[i] = arr[0]~arr[i]까지의 합의 최댓값

dp = [0 for i in range(N)]
if N >= 1:
    dp[0] = arr[0]
if N >= 2:
    dp[1] = arr[0]+arr[1]
if N >=3:
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])
# dp[2] = max(dp[0]+arr[2], dp[1]) 가 아닌 이유 : dp[i] : i번째 계단을 모두 지났을 경우를 고려하는 거니까!!!

    for i in range(3, N):
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
# print(dp)
print(dp[N-1])