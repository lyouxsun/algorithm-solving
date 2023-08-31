# 다이나믹 프로그래밍 - 11727번 - 2*n 타일링 2
import sys
input = sys.stdin.readline
N = int(input())
arr = [0 for i in range(N)]
arr[0] = 1
arr[1] = 3
if N == 1:
    arr[0] = 1
else:
    arr[1] = 3
    for i in range(2, N):
        arr[i] = arr[i-2]*2+arr[i-1]
print(arr[N-1] % 10007)