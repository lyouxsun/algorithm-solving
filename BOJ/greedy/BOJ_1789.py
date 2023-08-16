# 그리디 알고리즘 - 1789번 - 수들의 합
## 1부터 n까지의 합 > S 이면 n-1 출력하기
## (n+1) * n/2
import sys
S = int(sys.stdin.readline())
ans=0
for i in range(S):
    if S==1 or S==2:
        ans=1
        break
    if S==3:
        ans=2
        break
    if (i+1) * i/2 > S:
        ans = i-1
        break
print(ans)