# 그리디 알고리즘 - 1715번 - 카드 정렬하기
import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for i in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))
sum = 0

while len(heap)>1:
    tmp = heapq.heappop(heap)+heapq.heappop(heap)
    sum += tmp
    heapq.heappush(heap,tmp)
print(sum)