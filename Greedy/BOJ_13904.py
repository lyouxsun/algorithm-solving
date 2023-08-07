# 그리디 알고리즘 - 13904번 - 과제
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:-x[1])

day = 0
for i in range(N):
    if day < arr[i][0]:
        day = arr[i][0]
answer = [0 for i in range(day+1)]

for i in range(N):
    if answer[arr[0][0]] == 0:
        answer[arr[0][0]] = arr[0][1]
    else:
        for i in range(arr[0][0], 0, -1):
            if answer[i] == 0:
                answer[i] = arr[0][1]
                break
    del arr[0]
print(sum(answer))