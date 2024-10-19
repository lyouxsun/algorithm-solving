# 수학 - 1010번 - 다리놓기
import math
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    print(math.comb(max(n, m), min(n, m)))