# 그리디 알고리즘 - 1092번 - 배
import sys, heapq
input = sys.stdin.readline
N = int(input())
car = list(map(int, input().split()))
K = int(input())
jim = list(map(int, input().split()))
cnt=0
tmp = []

car.sort(key = lambda x:-x)
jim.sort(key = lambda x:-x)
print(car)
print(jim)
tmp1 = jim[0]
tmp2 = car[0]

while len(jim) > 0:
    for i in range(N):
        if car[i] >= jim[0]:
            del jim[0]
        else:
            tmp.append(jim[0])
            del jim[0]
    jim.extend(tmp)
    jim.sort(key=lambda x: -x)
    cnt+=1
if tmp1>tmp2:
    print("-1")
else:
    print(cnt)