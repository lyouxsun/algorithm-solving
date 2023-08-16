# 그리디 알고리즘 - 2217번 - 로프
## 리스트 중 최솟값 * 줄의 갯수
## 근데 (리스트에서 두번째로 작은 수)*(줄의 총개수-1)이랑 비교해야됨

import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

for i in range(N):
    arr[i] *= (N-i)
print(max(arr))