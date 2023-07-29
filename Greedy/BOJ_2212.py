# 그리디 알고리즘 - 2212번 - 센서
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
delete = 0
arr = list(map(int, input().split()))
arr.sort()
for i in range(0, N-1):
    if arr[i]==arr[i+1]:
        arr.append(arr[i+1])
        del arr[i + 1]
        delete += 1
        N -= 1
for _ in range(delete):
    arr.pop()

distance=[]
for i in range(0, N-1):
    distance.append(arr[i+1]-arr[i])
distance.sort(key=lambda x: -x)
del distance[:K-1]
print(sum(distance))