# 그리디 알고리즘 - 11000번 - 강의실 배정
## 일찍 끝나는 수업 먼저 pop -> 그전에 끝난 수업<=시작시간 인 수업 찾아서 push
import sys, heapq
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort()
end = 0
i = 0
cnt = 0
while arr:
    if arr[i][0]>=end:
        end = arr[0][1]
        del arr[0]
        i+=1
    else:
        cnt += 1
        i+=1


