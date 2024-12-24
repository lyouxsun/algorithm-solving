# 수학 - 15829번 - Hashing
import sys

input = sys.stdin.readline
M = 1234567891
r = 31

n = int(input())
input_num = list(input().strip())
arr = []
for i in input_num:
    arr.append(ord(i) - ord('a') + 1)
ans = 0
for i in range(n):
    ans += arr[i] * r ** i
print(ans % M)