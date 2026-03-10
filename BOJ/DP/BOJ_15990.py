# DP - 15990번 - 1,2,3 더하기 5
## dp[i][a] = 합이 i가 되는 조합 중, 마지막으로 더해진 수가 a인 경우의 수
import sys
input = sys.stdin.readline

T = int(input())
arr = [0] * T
for i in range(T):
    arr[i] = int(input())

SIZE = max(arr)
dp = [[0] * 4 for _ in range(max(SIZE + 1, 4))]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, SIZE + 1):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % 1000000009
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009

for i in range(T):
    N = arr[i]
    print((dp[N][1] + dp[N][2] + dp[N][3]) % 1000000009)
