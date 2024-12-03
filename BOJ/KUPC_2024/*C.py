# dp?
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] * (n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]
now = 0  # 이전에 더한 수
max_num = 0
max_idx = 0
if k < n:
    max_num = 0
    for i in range(k):
        if max_num < arr[i]:
            max_num = arr[i]
            max_idx = i
    tmp2 = arr[n - k:]
    for i in range(n-1, n-k, -1):
        if max_num <= arr[i]:
            max_num = arr[i]
            max_idx = i
else:
    for i in range(n):
        if max_num == arr[i]:
            if max_idx > n-1-i:
                max_idx = i
        elif max_num < arr[i]:
            max_num = arr[i]
            max_idx = i

cost, remain = 0, k
if max_idx == n - max_idx - 1:  # 양쪽모두 거리가 똑같을 때 -> 더 큰 방향으로 가기
    cost = max(prefix_sum[max_idx], prefix_sum[-1] - prefix_sum[max_idx+1])
    remain -= max_idx

elif max_idx > n - max_idx - 1:  # 역방향
    cost = prefix_sum[-1] - prefix_sum[max_idx]
    remain -= (n - max_idx)

else:  # 정방향
    cost = prefix_sum[max_idx]
    remain -= max_idx

if remain > 0:
    cost += remain * max_num

print(cost)

# 5 10
# 1 10 20 10 9

# 15 100
# 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9
