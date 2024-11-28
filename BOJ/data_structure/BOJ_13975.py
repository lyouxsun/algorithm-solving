# 우선순위큐 - 13975번 - 파일 합치기 3
import sys
from heapq import *

input = sys.stdin.readline

cycle = int(input())
for _ in range(cycle):
    n = int(input())
    q = list(map(int, input().split()))
    heapify(q)  # q를 리스트에서 힙으로 변환

    dp = [0] * n
    for i in range(1, n):
        cost = heappop(q) + heappop(q)
        dp[i] = dp[i-1] + cost
        # print('지금까지의 비용=', dp[i])
        heappush(q, cost)
    print(dp[-1])

