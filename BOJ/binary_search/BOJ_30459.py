# BinarySearch - 30459번 - 현수막 걸기
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
maldduk = list(map(int, input().split()))
height = list(map(int, input().split()))

maldduk.sort()
base = set()
for i in range(n - 1):
    for j in range(i, n):
        base.add(maldduk[j] - maldduk[i])
base = list(base)
base.sort()

answer = -1
for i in range(m):
    left = 0
    right = len(base) - 1
    while left <= right:
        mid = (left + right) // 2
        if base[mid] * height[i] <= 2 * r:
            answer = max(answer, base[mid] * height[i])
            left = mid + 1
        else:
            right = mid - 1

if answer > 0:
    print("%.1f" % (answer / 2))
else:
    print(-1)
