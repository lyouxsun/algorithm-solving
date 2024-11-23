# 홀수개로 나누기 -> 합이 홀수, 부분수열의 개수도 홀수

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 홀수로 나누기
if sum(arr) % 2 == 1:
    print(1)
    exit()

# 짝수로 나누기
tmp, cnt = 0, 0
prefix = [0] * n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]
for i in range(n-1):
    # print(prefix[i])
    # print(prefix[n-1] - prefix[i+1])
    if prefix[i] % 2 ==0 and (prefix[n-1] - prefix[i+1]) % 2 ==0:
        print(1)
        exit()
print(0)