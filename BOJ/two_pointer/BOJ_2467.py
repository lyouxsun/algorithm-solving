# 투포인터 - 2467번 - 용액
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
start, end = 0, N-1
diff = float('inf')
ans = []

while True:
    if start >= end:
        break
    # print('start=', start, ', end=', end)
    if abs(arr[start] + arr[end]) < abs(diff):
        # print('diff보다 작다!! start=', start, ', end=', end)
        ans.clear()
        ans.append(arr[start])
        ans.append(arr[end])
        diff = arr[start] + arr[end]
    if arr[start] + arr[end] >= 0:
        end -= 1
    else:
        start += 1

print(ans[0], ans[1])

# 반례 : 모두 음수인 경우
# 5
# -5 -4 -3 -2 -1