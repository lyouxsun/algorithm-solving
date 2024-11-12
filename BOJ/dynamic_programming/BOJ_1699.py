import sys
input = sys.stdin.readline

n = int(input())
root = 1
while True:
    if (root + 1) ** 2 > n:
        break
    root += 1

sqr = [i**2 for i in range(root+1)]
dp = [0 for _ in range(n+1)]
dp[1] = 1
# print(sqr)

for i in range(2, n+1):
    if i in sqr:
        dp[i] = 1
        continue
    j = root
    while True:
        if sqr[j] < i:
            break
        j -= 1

    candidate = dp[j ** 2] + dp[i - j ** 2]
    for k in range(j, 0, -1):
        tmp = dp[k ** 2] + dp[i - k ** 2]
        if candidate > tmp:
            candidate = tmp

    dp[i] = min(dp[i-1]+1, candidate)

# print(dp)
print(dp[n])