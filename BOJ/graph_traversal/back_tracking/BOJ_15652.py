# 백트래킹 - 15652번 - N과 M (4)
from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def tracking(last, length):
    global n, m
    if length == m:
        for i in last:
            print(i, end=' ')
        print()
        return
    for i in range(last[-1], n+1):
        # print(last+[i])
        tracking(last + [i], length+1)


for start in range(1, n+1):
    arr = [start]
    tracking(arr, 1)