# 그리디 알고리즘 - 1946번 - 신입사원
## 정렬 이용하기!!!
import sys
testCase = int(sys.stdin.readline())

for _ in range(testCase):
    N = int(sys.stdin.readline())
    arr = []
    cnt = 0
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))
    arr.sort(key=lambda x:x[0])
    minimum = N+1
    for i in range(N):
        if arr[i][1] < minimum:
            cnt += 1
            minimum = arr[i][1]
    print(cnt)