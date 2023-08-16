# 그리디 알고리즘 - 2109번 - 순회강연
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(reverse=True)
maxdate = 0
for i in range(N):
    if arr[i][1]>maxdate:
        maxdate = arr[i][1]
result = [0 for i in range(maxdate+1)]

for i in range(N):
    for j in range(arr[i][1], 0, -1):
        if result[j] == 0:
            result[j] = arr[i][0]
            break
print(sum(result))