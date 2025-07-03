# 동적 프로그래밍 - 11048번 - 이동하기
## 첫번째 방식은 바텀업 방식으로 풀었다면, 이번에는 탑다운 방식으로 풀기!!!
## 탑다운 방식에서는 메모이제이션이 가장 중요!!!

import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m+1)] for _ in range(n + 1)]


def go(i, j):
    if i < 1 or j < 1:
        return 0
    if dp[i][j] >= 0:  # dp를 0으로 초기화 할 경우 무한 재귀 호출이 될 수 있다.
        return dp[i][j]  # 메모이제이션 된 것 활용 -> 중복 연산 최소화
    dp[i][j] = max(go(i - 1, j), go(i, j - 1)) + arr[i-1][j-1]
    return dp[i][j]


## arr의 모든 수가 0 이상이니까 대각선은 고려하지 않아도 됨.

print(go(n, m))
