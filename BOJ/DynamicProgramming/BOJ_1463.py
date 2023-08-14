# 다이나믹 프로그래밍 - 1463번 - 1로 만들기
## 보텀업(반복문 : 1 -> N), 메모이제이션 기법 사용하기
import sys
input = sys.stdin.readline
N = int(input())
# i번째 리스트에는 i를 만들기 위해 걸렸던 최소 횟수 적기
dp = [0 for _ in range(N+1)]
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    # print(f"dp[{i}] = {dp[i]}")
print(dp[N])