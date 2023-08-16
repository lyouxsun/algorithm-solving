# 그리디 알고리즘 - 1781번 - 컵라면
import sys, heapq   # 디폴트가 최소힙 (heappush하면 최솟값이 나온다.)
input = sys.stdin.readline
N = int(input())
arr = []
maxN = 0
for _ in range(N):
    n, m = map(int, input().split())
    arr.append([n, m])
    maxN = max(n, maxN)
arr.sort()
heap = []
for i in arr:
    heapq.heappush(heap, i[1])
    if len(heap)>i[0]:
        heapq.heappop(heap)
print(sum(heap))