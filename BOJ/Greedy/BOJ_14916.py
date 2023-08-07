# 그리디 알고리즘 - 14916 - 거스름돈
import sys
input = sys.stdin.readline
N = int(input())
cnt = N//5
N %= 5

if cnt>0 and N%2==1:
    N+=5
    cnt-=1
cnt += N//2
N %= 2
if N>0:
    print("-1")
else:
    print(cnt)
