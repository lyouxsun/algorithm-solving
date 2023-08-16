# 그리디 알고리즘 - 1092번 - 배
import sys, heapq
input = sys.stdin.readline
N = int(input())
car = list(map(int, input().split()))
K = int(input())
jim = list(map(int, input().split()))
car.sort(reverse=True)
jim.sort(reverse=True)
cnt=0

if car[0] < jim[0]:
    print("-1")
else:
    while jim:
        tmp = car[:]
        # print(tmp)
        # print(jim)
        i=0
        while tmp and len(jim)>i:
            if tmp[0] >= jim[i]:
                del tmp[0]
                del jim[i]
            else:
                i += 1
        cnt += 1
    print(cnt)