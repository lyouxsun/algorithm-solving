# 그리디 알고리즘 - 11000번 - 강의실 배정
## 일찍 끝나는 수업 먼저 pop -> 그전에 끝난 수업<=시작시간 인 수업 찾아서 push
import sys, heapq
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    heapq.heappush(arr, list(map(int, input().split())))
end = [0]
cnt = 1
for i in range(N):
    if arr[0][0] >= end[0]:
        heapq.heappop(end)
    else:
        cnt += 1
    heapq.heappush(end, arr[0][1])
    heapq.heappop(arr)
print(cnt)

