# 이분 탐색 - 12015번 - 이분 탐색
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [arr[0]]


def binary_search(ans, target):
    start, end = 0, len(ans) - 1
    while start < end:
        mid = (start + end) // 2
        if ans[mid] == target:
            return mid
        elif ans[mid-1] < target < ans[mid]:
            return mid
        elif target < ans[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start



for i in range(1, n):
    # print('i=', i, ' , ', ans)
    if ans[-1] < arr[i]:
        ans.append(arr[i])
    else:
        idx = binary_search(ans, arr[i])
        ans[idx] = arr[i]
# print(ans)
print(len(ans))

# 9
# 6 4 3 6 3 6 9 7 8
# 답 = 4