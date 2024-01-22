import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# profit = []
#
# for i in range(n):
#     for j in range(i):
#         if arr[i]-arr[j]>0:
#             profit.append(arr[i]-arr[j])
# if len(profit) == 0:
#     print('0')
# else:
#     print(max(profit))

# profit을 배열로 만들 필요 없이 변수로 만들어서 비교하는게 더 좋음! (메모리도 덜 잡아먹고!!)
profit = 0

for i in range(n):
    for j in range(i):
        if arr[i]-arr[j] > profit:
            profit = arr[i]-arr[j]
print(profit)