# 311 - 모험가 길드
## 아이디어 :
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
tmp = 0
for i in range(len(arr)):
    tmp += 1
    if tmp >= arr[i]:
        cnt += 1
        tmp = 0
print(cnt)