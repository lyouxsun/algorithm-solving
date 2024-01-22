import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

arr1 = arr.sort()
print(arr[-1], arr[-2])