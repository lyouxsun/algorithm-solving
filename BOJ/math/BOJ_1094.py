n = int(input())
arr = [2**i for i in range(6, -1, -1)]

answer = 0
for i in arr:
    if i <= n:
        n -= i
        answer += 1

print(answer)
