# 동적 프로그래밍 - 11052번 - 카드 구매하기
## 구해야 하는 거 : i개의 카드 가격의 최댓값
## dp[i] = 카드를 i개 살 때 최대 비용

n = int(input())
arr = [0] + list(map(int, input().split()))     # 인덱스 1부터 입력받는 방법
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = arr[i]
    for j in range(i//2+1):
        dp[i] = max(dp[i], dp[i-j]+dp[j])

# print(dp)
print(dp[n])