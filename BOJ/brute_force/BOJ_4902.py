# 브루트 포스 - 4902번 - 삼각형의 값
from collections import deque
import sys

input = sys.stdin.readline
ans = 0
cycle = 1


# h - 전체 높이, arr - 주어진 삼각형 전체 숫자 배열
def calc(r, c1, c2, sum):  # 부분 삼각형의 가장 뚱뚱한 부분 양쪽 좌표 = r행 c1열 ~ r행 c2열 & 지금까지의 합
    if not (1 <= r <= n):
        return
    if not (1 <= c1 <= 2 * r - 1) or not (1 <= c2 <= 2 * r - 1):
        return
    # print('%d행 %d열부터 %d열까지를 더하기 전 sum = %d' % (r, c1, c2, sum))

    sum += rec[r][c2] - rec[r][c1 - 1]
    global ans
    # if sum > ans:
    #     print('[ans 바뀜]%d행 %d열부터 %d열까지 => %d'%(r, c1, c2, sum))
    ans = max(ans, sum)
    if c1 % 2 == 0:  # 거꾸로 서있는 삼각형
        calc(r - 1, c1 - 2, c2, sum)
    else:  # 제대로 서있는 삼각형
        calc(r + 1, c1, c2 + 2, sum)
    return


while True:
    arr = deque(map(int, input().split()))
    if arr[0] == 0:
        break
    n = arr.popleft()
    rec = [[0] for i in range(n + 1)]

    rec[1].append(arr.popleft())

    ans = float('-INF')
    for i in range(2, n + 1):
        for j in range(2 * (i - 1) + 1):
            rec[i].append(rec[i][-1] + arr.popleft())  # 각 행의 누적합을 저장
    # for i in range(1, n + 1):
    #     print(rec[i])
    for i in range(1, n + 1):
        for j in range(1, 2 * i):  # i행에는 2*i-1 개의 수만 존재한다.
            calc(i, j, j, 0)  # 부분 삼각형의 가장 뚱뚱한 부분 양쪽 좌표
    print('%d. %d' % (cycle, ans))
    cycle += 1
