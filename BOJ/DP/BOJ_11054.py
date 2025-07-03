# 동적 프로그래밍 - 11054번 - 가장 긴 바이토닉 부분 수열
## 해결 방법 : arr[i] 를 포함하는 증가했다-감소하는 수열 (바이토닉 수열)의 최대길이 찾아서 dp테이블에 저장 -> 바이토닉 수열 이어 나가기!

#                                       input arr : 1 5 2 1 4 3 4 5 2 1
# (1) arr[0] ~ arr[i], arr[i]를 포함하면서 증가하는 수열 : 1 2 2 1 3 3 4 5 2 1 (0부터 구해야함)
# (2) arr[i] ~ arr[N], arr[i]를 포함하면서 감소하는 수열 : 1 5 2 1 4 3 3 3 2 1 (N부터 구해야함)
#                                답 = (1) + (2) -1 : 2 7 4 2 7 6 7 8 4 2

N = int(input())
arr = list(map(int, input().split()))
dp1 = [1 for _ in range(N)]  # (1)
dp2 = [1 for _ in range(N)]  # (2)

# (1)
for i in range(N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

# (2)
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)


# (1)+(2)-1
for i in range(N):
    dp1[i] = dp1[i] + dp2[i] - 1

print(max(dp1))