# 백트래킹 - 15666번 - N과 M (12)
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
set_ = set(map(int, input().split()))
arr = list(set_)
arr.sort()
n = len(arr)

## sol1. 재귀를 사용하여 중복순열 만들기  -> 알고리즘(백트래킹)에 맞는 풀이
def make_ans(ans, idx, cnt):
    global n, m, arr
    if cnt == m:
        for i in ans:
            print(i, end = ' ')
        print()
        return
    cnt += 1
    for j in range(idx, n):
        ans.append(arr[j])
        # print('ans=', ans, ', j=', j)
        make_ans(ans, j, cnt)
        ans.pop(-1)


# print(arr)
for i in range(n):
    ans = []
    ans.append(arr[i])
    make_ans(ans, i, 1)

## sol2. itertools를 사용한 간단한 풀이 -> 더 간단한 풀이 (둘다 시간과 메모리 사용량은 비슷함)
c = combinations_with_replacement(arr, m)
for i in c:
    ans = list(i)
    for j in ans:
        print(j, end = ' ')
    print()
