# 동적 프로그래밍 - 14002번 - 가장 긴 증가하는 부분 수열 4
## 이전 문제들과 달리 길이&부분수열 모두를 출력해야 한다.

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
prev_index = [-1] * N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
            prev_index[i] = j
# print(dp)

max_len = max(dp)
max_idx = dp.index(max_len)
ans = []

while max_idx != -1:
    ans.append(arr[max_idx])
    max_idx = prev_index[max_idx]

ans.reverse()

print(max_len)
print(" ".join(map(str, ans)))