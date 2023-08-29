# 그리디 알고리즘 - 1783번 - 병든 나이트
import sys
input = sys.stdin.readline
x, y = map(int, input().split())
if x==1:
    answer = 1
elif x==2:
    answer = min(4, (y+1)//2)
else:
    if y>6:
        answer = y-2
    else:
        answer = min(4, y)
print(answer)