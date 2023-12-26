# 그래프 이론 - 1697번 - 숨바꼭질
import sys
N, K = map(int, sys.stdin.readline().split())
if K <= N:
    print(N-K)
    exit(0)

cnt = 0
s = {N}
while True:
    cnt += 1
    tmp = s.copy()
    s.clear()
    for i in tmp:
        if i < K:
            s.add(i*2)
            s.add(i + 1)
        if i > K//2:
            s.add(i-1)
    # print(s, '\n-----------------------------\n')
    if K in s:
        break
print(cnt)