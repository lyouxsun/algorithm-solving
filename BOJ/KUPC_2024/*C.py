# dp?
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
now = 0  # 이전에 더한 수
maximum = max(arr)
dp = [0] * (k + 1)

if arr[-1] > arr[0]:
    now = (now - 1 + n) % n
    dp[1] = arr[now]
else:
    # now = 0
    dp[1] = arr[now]

# now , now-1 이렇게만 가능
for i in range(2, k+1):
    cand1 = now
    cand2 = (now - 1 + n) % n
    if arr[cand1] > arr[cand2]:
        now = cand1
        dp[i] += arr[now]
    else:
        now = cand2
        dp[i] = arr[cand2]
    print(now)
print(dp)