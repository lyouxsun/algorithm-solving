import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

maximum = max(arr)
while maximum != arr[0]:
    idx = arr.index(maximum)
    print(idx+1, end=' ')
    arr = arr[:idx]
    maximum = max(arr)
idx = arr.index(maximum)
print(idx+1, end=' ')