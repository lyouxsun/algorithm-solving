# 투포인터 - 1806번 - 부분합
## 엄청나게 큰 1차원 배열 (1만 이상)의 부분, 전체 합을 구하는 문제에서 부분합&투포인터를 사용하자!!
## 완전탐색으로 해결하면 시간초과가 나는 경우 -> 투 포인터 알고리즘!!!

## sol1) 투포인터 적용 전 : 이중 반복문 때문에 시간초과 발생
# import sys
# input = sys.stdin.readline
#
# n, limit = map(int, input().split())
# arr = list(map(int, input().split()))
# for i in range(1, n):
#     arr[i] = arr[i - 1] + arr[i]
# if arr[0] >= limit:
#     print(1)
#     exit()
# for l in range(n):
#     for i in range(n-l):
#         if arr[i+l] - arr[i] >= limit:
#             print(l)
#             exit()
# print(0)

import sys
input = sys.stdin.readline

n, limit = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n):
    arr[i] = arr[i - 1] + arr[i]
arr.insert(0, 0)
if arr[0] >= limit:
    print(1)
    exit()
# print('arr=', arr)
start, end = 0, 0
ans = float('INF')
while end <= n:
    if arr[end] - arr[start] >= limit:
        # print('start=%d, end=%d, result=%d'%(start, end, end-start))
        ans = min(ans, end-start)
        start += 1
    elif arr[end] - arr[start] < limit:
        # print('start=%d, end=%d'%(start, end))
        end += 1

if ans == float('INF'):
    print(0)
    exit()
print(ans)

# 반례
# 10 10
# 1 1 1 1 1 1 1 1 1 1

## 주의 : 배열 전체를 더해야만 답을 찾을 수 있는 경우를 대비해서 0번째 인덱스에는 0값을 insert 해야한다!
##       -> 그래야 0번째 인덱스의 수까지 포함하여 계산할 수 있다.