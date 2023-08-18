# 다이나믹 프로그래밍 - 1149번 - RGB거리
import sys
input = sys.stdin.readline
N = int(input())
arr = []
answer = [0 for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

# answer = arr[i] 가 R일때, G일때, B일때 각각의 경우의 최솟값을 저장
for i in range(1, N):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])
print(min(arr[i][0], arr[i][1], arr[i][2]))