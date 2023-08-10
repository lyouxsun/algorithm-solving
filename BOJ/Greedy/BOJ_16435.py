# 그리디 알고리듬 - 16435번 - 스네이크버드
import sys
input = sys.stdin.readline
N, start = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in arr:
    if i <= start:
        start += 1
    else:
        break
print(start)