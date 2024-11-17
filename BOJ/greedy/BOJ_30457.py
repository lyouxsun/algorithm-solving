# 그리디 - 30457번 - 단체 줄넘기
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
remain = []

last = 0
for i in range(n):
    if last < arr[i]:
        answer += 1
        last = arr[i]
    else:
        remain.append(arr[i])

print(answer + len(set(remain)))