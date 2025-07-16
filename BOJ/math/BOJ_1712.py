import sys

A, B, C = map(int, input().split())
profit = C - B
if profit <= 0:
    print(-1)
    sys.exit()
i = 0
while True:
    if A < profit * i:
        print(i)
        break
    i += 1
        