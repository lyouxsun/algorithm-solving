# 2960번 - 구현 - 에라토스테네스의 체

n, k = map(int, input().split())
arr = [0 for _ in range(n + 1)]
ans = []
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if arr[j] == 0:
            arr[j] = 1
            ans.append(j)
    if len(ans) >= k:
        break
print(ans[k - 1])
