import sys
import math

n = int(sys.stdin.readline().rstrip())

if n == 0:
    print(0)
else:
    arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    arr.sort()
    border = int(n * 0.15 + 0.5)
    trimmed = arr[border:n-border]
    avg = sum(trimmed) / len(trimmed)
    print(math.ceil(avg) if avg - int(avg) >= 0.5 else int(avg))