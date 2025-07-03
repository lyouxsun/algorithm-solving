# 동적 프로그래밍 - 15486번 - 퇴사2
import sys
input = sys.stdin.readline

n = int(input())
t = [0] * n
p = [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())
# dp = [arr[i][1] for i in range(n)]
dp = [0 for _ in range(n+50)]

for i in range(n):
    dp[i + t[i]] = max(dp[i+t[i]], dp[i]+p[i])      # i번째 날에 잡힌 일을 하는 경우
    dp[i+1] = max(dp[i], dp[i+1])                   # i번째 날에 잡힌 일을 하지 않는 경우

# print(dp)
print(dp[n])
