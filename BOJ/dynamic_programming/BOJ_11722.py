# 동적 프로그래밍 - 11722번 - 가장 긴 감소하는 부분 수열
## 해결 방법 : arr[i] 를 포함하는 감소하는 수열의 최대길이 찾아서 dp테이블에 저장 -> 감소수열을 이어 나가기!

N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(0, i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
# dp[i] : arr[i] 를 포함한 감소 수열 중 가장 긴 수열의 길이
print(max(dp))

# 5 7 2 3 5 6 8 1 3 1 2 2 1
# 1 1 2 2 2 2 1 3 3 4 4 4 5 -> 5