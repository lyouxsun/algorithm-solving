# 동적 프로그래밍 - 11055번 - 가장 큰 증가하는 부분 수열
## 증가하는 부분수열, 그 중 합이 가장 큰거!
## 해결방법 : arr[i] 를 포함하는 증가 수열 중 최대 합을 dp테이블에 저장

# 1 100   2    50    60    3                101                   7    4000 -> 이렇게 차이나게 큰 값이 나오면 조건문 속 max() 에서 dp[i] 가 선택됨
# 1 101   3    53   113    6    (arr[j] 가 50일 때) 201 vs 151     13    4000
#                               (arr[j] 가 60일 때) 201 vs 214

N = int(input())
arr = list(map(int, input().split()))
dp = [arr[i] for i in range(N)]         # dp에는 arr 값 그대로 넣어주기
for i in range(N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))
