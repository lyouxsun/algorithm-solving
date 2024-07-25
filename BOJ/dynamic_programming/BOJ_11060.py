# 동적 프로그래밍 - 11060 - 점프점프
## 1. 지금 dp[i] 는 어디서부터 온 것일까
## 2. 지금 dp[j] 는 어디로 가야 최적일까

n = int(input())
arr = list(map(int, input().split()))
dp = [float("inf")] * n
dp[0] = 0
if n == 1:
    print(0)
    exit()

if arr[0] == 0:
    print(-1)
    exit()

for i in range(n):
    for j in range(arr[i]+1):
        if i + j >= n:
            continue
        dp[i+j] = min(dp[i+j], dp[i]+1)

# print(dp)
if dp[n-1] == float("inf"):
    print(-1)
else:
    print(dp[n-1])
