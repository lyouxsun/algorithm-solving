# 다이나믹 프로그래밍 - 9095번 - 1,2,3 더하기
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
answer = [0 for _ in range(max(arr)+1)]
answer[1] = 1
answer[2] = 2
answer[3] = 4
for i in range(4, max(arr)+1):
    answer[i] = answer[i-1] + answer[i-2] + answer[i-3]
for i in arr:
    print(answer[i])