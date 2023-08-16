# 동적 프로그래밍 - 1003번 - 피보나치 함수 (이 문제는 보텀업 풀이인듯!!)
import sys
input = sys.stdin.readline
N = int(input())
arr = [[0 for j in range(2)] for i in range(41)]
arr[0] = [1, 0]
arr[1] = [0, 1]

sol = []
for _ in range(N):
    sol.append(int(input()))
maximum = max(sol)
for i in range(2, maximum+1):
    arr[i][0] = arr[i-2][0]+arr[i-1][0]
    arr[i][1] = arr[i-2][1]+arr[i-1][1]
for j in range(N):
    i = sol[j]
    print(arr[i][0], arr[i][1])