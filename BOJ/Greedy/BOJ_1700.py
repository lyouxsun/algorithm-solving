# 그리디 알고리즘 - 1700번 - 멀티탭 스케줄링
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
tmp = []
while len(tmp)<N and len(arr)>0:
    if arr[0] not in tmp:
        tmp.append(arr[0])
    del arr[0]
if len(arr)>0:
    for i in range(len(arr)):
        if arr[0] not in tmp:
            sig = False
            # tmp중 다음에 쓰이지 않는 수가 하나라도 있을 때
            for i in tmp:
                if i not in arr:
                    del tmp[tmp.index(i)]
                    cnt += 1
                    sig = True
                    break
            if sig == False:
                # tmp가 모두 다음에 한번이라도 쓰일 때 -> tmp 수들의 arr index가
                max = 0
                for i in tmp:
                    if arr.index(i) >= max:
                        max = arr.index(i)
                del tmp[tmp.index(arr[max])]
                cnt += 1
            tmp.append(arr[0])
        del arr[0]
print(cnt)