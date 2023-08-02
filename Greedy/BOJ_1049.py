# 그리디 알고리즘 - 1049번 - 기타줄
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
set = []
one = []
total = [] #1. 묶음으로만 샀을때 // 2.딱맞춰서 묶음+낱개로 샀을 때 // 3.낱개로만 샀을때
for i in range(M):
    tmp1, tmp2 = map(int, input().split())
    set.append(tmp1)
    one.append(tmp2)
minOne = min(one)
minSet = min(set)
if N%6==0:
    setNum = N//6
else:
    setNum = N//6+1
total.append(minSet*setNum)     # 1. 묶음으로만 샀을때
total.append(minSet*(N//6) + minOne*(N%6))      # 2.딱맞춰서 묶음+낱개로 샀을 때
total.append(minOne*N)
print(min(total))
