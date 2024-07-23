# 동적 프로그래밍 - 14002번 - 가장 긴 증가하는 부분 수열 4
## 이전 문제들과 달리 길이&부분수열 모두를 출력해야 한다.

## 10 20 10 30 20 50
## 10 20    30


N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(dp)

# ans_len = 0
# ans_index = 0
# for i in range(N):
#     if len(dp[i]) > ans_len:
#         ans_len = len(dp[i])
#         ans_index = i
#
# print(ans_len)
# print(dp[ans_index])