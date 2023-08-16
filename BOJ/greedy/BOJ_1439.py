# 그리디 알고리즘 - 1439번 - 뒤집기
import sys
N = sys.stdin.readline()
arr = list(N)
cnt0 = 0
cnt1 = 0
if arr[0] == '0':
    cnt0 += 1
else:
    cnt1 += 1
for i in range(len(arr)):
    if arr[i] == '0' and arr[i+1] == '1':
        cnt1 += 1
    elif arr[i] == '1' and arr[i+1] == '0':
        cnt0 += 1
if (cnt0 == 0 and cnt1 == 1) or (cnt1 == 0 and cnt0 == 1):
    print(0)
elif cnt1 == 0 and cnt0 != 0:
    print(cnt0)
elif cnt0 == 0 and cnt1 != 0:
    print(cnt1)
else:
    print(min(cnt0, cnt1))
