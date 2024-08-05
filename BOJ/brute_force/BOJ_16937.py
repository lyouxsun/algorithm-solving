# 브루트 포스 - 16937번 - 두 스티커
h, w = map(int, input().split())
n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = list(map(int, input().split()))

ans = 0
for i in range(n):
    h1, w1 = arr[i]
    for j in range(i + 1, n):
        h2, w2 = arr[j]
        for _ in range(2):
            for _ in range(2):
                if h1 + h2 <= h and max(w1, w2) <= w:
                    ans = max(ans, h1 * w1 + h2 * w2)
                    # print(h1, w1, h2, w2)
                elif w1 + w2 <= w and max(h1, h2) <= h:
                    ans = max(ans, h1 * w1 + h2 * w2)
                    # print(h1, w1, h2, w2)
                h1, w1 = w1, h1
            h2, w2 = w2, h2

print(ans)
