# # ?? - 32713번 - 숫자 POP
# ## 1. 각 수가 몇개 있는지를 dict에 저장
# ## 2. 개수가 많은 수부터 차례대로 투포인터를 써서 사이 원소들 지우기
#
# import sys
# input = sys.stdin.readline
# n, pop_num = map(int, input().split())
# arr = list(map(int, input().split()))
# d = dict()
#
# for i in arr:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# sorted_d = sorted(d.items(), key= lambda item:item[1], reverse = True)
# # print(sorted_d)
# ans = 0
#
# for (k, v) in sorted_d:
#     idx_arr = []
#     cnt = 0
#     for i in range(n):
#         if arr[i] == k:
#             idx_arr.append(i)
#             cnt += 1
#     # print('key =', k, ', ', idx_arr)
#
#     # 최대한 pop해보기
#     result, tmp = 0, 1
#     remain = pop_num
#     # print('remain=', remain)
#     for j in range(1, cnt):
#         next, now = idx_arr[j], idx_arr[j-1]
#         if next == now +1:
#             tmp += 1
#         else:
#             # print('next - now -1=', next - now -1)
#             # print('remain=', remain)
#             if next - now -1 <= remain:
#                 remain -= (next - now -1)
#                 tmp += 1
#             else:
#                 result = max(result, tmp)
#                 tmp = 1
#                 remain = pop_num
#         # print('j=', j, ', tmp=', tmp)
#     result = max(result, tmp)
#     # print(result)
#     # pop 한 후의 최대 연속 길이 구하기
#     ans = max(ans, result)
#     # print()
#
# print(ans)

import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    arr.sort()
    if arr[0] * arr[0] + arr[1] * arr[1] == arr[2] * arr[2]:
        print("right")
    else:
        print("wrong")