# 중간에서 만나기 - 2143번 - 두 배열의 합
## 1208번과 달리, 연속된 수열의 합만 구하면 된다!
import sys

input = sys.stdin.readline

t = int(input())

n = int(input())
tmp1 = list(map(int, input().split()))
m = int(input())
tmp2 = list(map(int, input().split()))

## 1. 배열을 누적합으로 저장하기
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = a[i - 1] + tmp1[i - 1]

b = [0] * (m + 1)
for i in range(1, m + 1):
    b[i] = b[i - 1] + tmp2[i - 1]


def sum_comb(arr):
    sums = []
    n = len(arr)
    for i in range(1, n):  # i : 부분수열의 길이
        for j in range(n):  # j : 부분수열의 시작 인덱스
            if j + i < n:
                sums.append(arr[j + i] - arr[j])
    return sums


a_sums = sum_comb(a)
b_sums = sum_comb(b)

# print('a_sums = ', a_sums)
# print('b_sums = ', b_sums)

a_sums.sort()
b_sums.sort(reverse=True)

ap, bp = 0, 0  # a_sums, b_sums의 포인터
cnt = 0
while ap < len(a_sums) and bp < len(b_sums):
    current_sum = a_sums[ap] + b_sums[bp]
    if current_sum == t:
        ca = 1
        cb = 1
        ap += 1
        bp += 1
        while ap < len(a_sums) and a_sums[ap] == a_sums[ap - 1]:
            ca += 1
            ap += 1
        while bp < len(b_sums) and b_sums[bp] == b_sums[bp - 1]:
            cb += 1
            bp += 1
        cnt += ca * cb

    elif current_sum < t:
        ap += 1
    else:
        bp += 1

print(cnt)