# DP - 1106번 - 호텔
## dp[i] = 0~i번째 도시까지 고려했을 때 최소비용
import sys
input = sys.stdin.readline

C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     print(arr[i][1] / arr[i][0])

# 가성비 순으로 정렬 (만약 값이 동일하면, x[0] 이 작은게 더 먼저 오도록 정렬)
arr.sort(key=lambda x: (x[0] / x[1], -x[0]), reverse = True)
ans = 0
remain_client = C
if C % arr[0][1] == 0:
    m = C // arr[0][1]
    if m == 0:
        print(arr[0][0])
    else:
        print(arr[0][0] * m)
    sys.exit()

dp = [float('inf')] * N  # 0행에는 최종 비용, 1행에는 남은 고객 수 저장
m = C // arr[0][1]
dp[0] = (m + 1) * arr[0][0]

for i in range(1, N):
    cost, client = arr[i][0], arr[i][1]
    total_cost, m = 0, 1
    while True:
        if client * m <= C:
            total_cost += cost * m
            remain_client = C - client * m
            dp[i] = min(dp[i], total_cost)
            m+=1
        else:
            break
    remain_client = dp[1][i]
    m = remain_client // client
    if remain_client % client == 0:
        dp[0][i] = min(dp[0][i] + cost * m, dp[0][i - 1])
        break
    else:
        if dp[0][i] + cost * (m + 1) < dp[0][i - 1]:
            dp[0][i] = dp[0][i] + cost * (m + 1)
            if i + 1 < N:
                dp[0][i + 1] = dp[0][i] - cost
                dp[1][i+1] = dp[1][i] - client * m
        else:
            dp[0][i] = dp[0][i-1]
            if i + 1 < N:
                dp[0][i+1] = dp[0][i]
                dp[1][i+1] = dp[1][i]

print('정렬한 arr = ', arr)
print("===== dp =====")
print(dp[0])
print(dp[1])
print("==============\n")

if min(dp[0]) == 0:
    print(arr[0][0])
else:
    print(min(dp[0]))
# 반례 1
# input:
# 100 3
# 7 12
# 20 30
# 30 60
#
# answer:
# 57
#
# 반례 2
# input:
# 100 2
# 7 12
# 20 30
#
# answer:
# 67