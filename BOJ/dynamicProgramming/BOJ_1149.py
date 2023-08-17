# 다이나믹 프로그래밍 - 1149번 - RGB거리
import sys
input = sys.stdin.readline
N = int(input())
arr = []
answer = [[0 for _ in range(2)] for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

# for i in range(0, N):
#     tmp = {arr[i][0]:0, arr[i][1]:1, arr[i][2]:2}
#     answer[i][0] = tmp[min(arr[i])]
#     del tmp[max(arr[i])]
#     answer[i][1] = tmp[max(tmp.keys())]
# total = answer[]
# for i in range(1, N):
#     if answer[i][0]!=answer[i-1][0]:
#         if answer[i][0]!= answer[i+1][0]:
for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
print(min(arr[i][0], arr[i][1], arr[i][2]))