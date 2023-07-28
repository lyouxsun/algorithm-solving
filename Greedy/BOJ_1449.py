# 그리디 알고리즘 - 1449번 - 수리공 항승
## L-1 차이나는 거까지는 스티커 하나로 커버 가능!
import sys
input = sys.stdin.readline
N, L = map(int, input().split())
cnt = 1
arr = list(map(int, input().split()))
arr.sort()
while arr:
    tmp = arr[0]
    for i in range(len(arr)):
        if arr[0] <= tmp+L-1:
            del arr[0]
        else:
            cnt += 1
            break
print(cnt)