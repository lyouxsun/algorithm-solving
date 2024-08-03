# 브루트 포스 - 2003번 - 수들의 합2
## 근데 브루트포스로 하면 시간초과 나와서 투 포인터로 풂!

n,m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
start, end = 0, 0

while start <= end <= n:
    arr_sum = sum(arr[start:end])
    if arr_sum == m:
        ans += 1
        start += 1
    elif arr_sum > m:
        start += 1
    else:
        end += 1

print(ans)