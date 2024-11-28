# dp - 30460번 - 스위치
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.append(0)
arr.append(0)
dp = [0, arr[0], arr[0]+arr[1]]

for i in range(2, n+2):
    dp.append(max(dp[-1] + arr[i], dp[-3] + 2 * (arr[i] + arr[i-1] + arr[i-2])))

# print(dp)
print(dp[-1])

# three_dp = [0] * n
#
# for i in range(n - 2):
#     three_dp[i] = arr[i] + arr[i + 1] + arr[i + 2]
#
# three_dp[n - 2] = arr[n - 2] + arr[n - 1]
# three_dp[n - 1] = arr[n - 1]
#
# # print('three_dp =', three_dp)
# answer = 0
# now = 0
# while now < n - 2:
#     if arr[now] > 0 and arr[now + 1] > 0 and arr[now + 2] > 0:
#         # print('2배, ', now)
#         answer += 2 * three_dp[now]
#         now += 3
#     elif 0 < three_dp[now] == max(three_dp[now], three_dp[now + 1], three_dp[now + 2]):
#         # print('2배, ', now)
#         answer += 2 * three_dp[now]
#         now += 3
#     else:
#         # print('그냥 더함, ', now)
#         answer += arr[now]
#         now += 1
#
# def remain(now):
#     global answer
#     r = n - now
#     if arr[now] > 0 and three_dp[now] > 0:
#         # print('2배, ', now)
#         answer += 2 * three_dp[now]
#         now += r
#     else:
#         # print('그냥 더함, ', now)
#         answer += arr[now]
#         now += 1
#     return now
#
# if now == n - 2:
#     now = remain(now)
# if now == n - 1:
#     now = remain(now)
#
# print(answer)