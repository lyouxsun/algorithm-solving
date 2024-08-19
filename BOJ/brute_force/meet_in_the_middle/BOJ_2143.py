# 중간에서 만나기 - 2143번 - 두 배열의 합
## 1208번과 달리, 연속된 수열의 합만 구하면 된다!
import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
n = int(input())
tmp1 = list(map(int, input().split()))
m = int(input())
tmp2 = list(map(int, input().split()))


## 1. 배열을 누적합으로 저장하기
def prefix_sum(arr):
    n = len(arr)
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i - 1]
    return prefix_sums


a = prefix_sum(tmp1)
b = prefix_sum(tmp2)


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
b_sums.sort()
c = Counter(b_sums)  # 각 요소가 b_sums 안에 몇개 있는지 dictionary 형태로 저장
cnt = 0
for num in a_sums:
    cnt += c[t - num]

print(cnt)
