# DP - 11066번 - 파일 합치기
import sys
input = sys.stdin.readline
cycle = int(input())

for _ in range(cycle):
    n = int(input())
    arr = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    dp = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):  # 부분 수열의 길이
        for start in range(n - l + 1):  # 부분 수열 시작 인덱스
            end = start + l - 1
            dp[start][end] = float('inf')
            for k in range(start, end):
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][k] + dp[k + 1][end] + prefix_sum[end + 1] - prefix_sum[start]
                )
    print(dp[0][n - 1])
