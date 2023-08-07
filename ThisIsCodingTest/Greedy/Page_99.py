# 99p - 1이 될 때까지
## 아이디어 :
import sys
sys = sys.stdin.readline
N, K = map(int, input().split())
cnt = 0
while N!=1:
    if N % K == 0:
        N /= K
        cnt += 1
    else:
        N -= 1
        cnt += 1
print(cnt)