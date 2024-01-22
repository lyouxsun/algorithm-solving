import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dif = 100
for i in range(n-1):
    if arr[i+1] - arr[i] < dif:
        dif = arr[i+1] - arr[i]
print(dif)