import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

small_max, large_min = 0, 1000
for i in arr:
    if i > 500:
        if large_min > i:
            large_min = i
    else:
        if small_max < i:
            small_max = i
print(small_max, large_min)