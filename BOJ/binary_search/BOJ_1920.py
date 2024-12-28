# 이분 탐색 - 1920번 - 수 찾기
import sys
input = sys.stdin.readline

n1 = int(input())
set1 = set(map(int, input().split()))
arr1 = list(set1)
n1 = len(arr1)
arr1.sort()

n2 = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    start, end = 0, n1-1
    flag = True
    while start<=end:
        idx = (start+end)//2
        # print('i=', i, ', idx=', idx, ', s=', start, ',end=',end )
        if arr1[idx] == i:
            print(1)
            flag = False
            break          
        if i > arr1[idx]:
            start = idx+1
            continue
        else:
            end = idx-1
            continue
    if flag:
        print(0)
        # print(i, idx, 0)

