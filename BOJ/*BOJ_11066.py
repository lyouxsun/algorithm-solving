# DP - 11066번 - 파일 합치기
## 총합 : 268
# 1 267 / 22 246 / 25 243 / 29 239 / 34 234 / 69 199 / 74 194
# 78 190 / 81 187 / 86 182 / 184 84 / 205 63 / 219 49 / 236 32
## 둘로 쪼갤 때, 둘의 차가 최소가 되도록! 쪼개줌

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def divide(arr, start, end, dp):
    if start>end:
        # print("오류")
        return
    if start == end:
        return 0
    if start+1 == end:
        dp[start][end] = arr[start] + arr[end]
        return dp[start][end]
    if dp[start][end] != -1:
        return dp[start][end]
    idx = 0
    ans = dp[start][end]
    arr_sum = sum(arr[start:end + 1])
    for i in range(start, end):
        tmp = divide(arr, start, i, dp) + divide(arr, i+1, end, dp) + arr_sum
        if ans == - 1 or tmp < ans:
            ans = tmp
            # idx = i
    # print("start:", start, " / end:", end, " 리턴값 : ", ans)
    # print(arr[start:idx], " / ", arr[idx:end+1])
    return ans


n = int(input())
for i in range(n):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    dp = [[-1] * 501 for _ in range(501)]
    print(divide(arr, 0, arr_len-1, dp))