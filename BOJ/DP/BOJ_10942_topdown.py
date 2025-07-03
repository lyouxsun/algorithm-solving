# 동적 프로그래밍 - 10942번 - 팰린드롬?
## 재귀, 탑다운 방식!!! 메모리 초과 발생..

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[-1 for _ in range(n)] for _ in range(n)]  # 각 자리를 중심으로 하는 팰린드롬의 반지름 길이 저장

for i in range(n):
    dp[i][i] = 1


# arr에서 팰린드롬인 부분 확인, 메모이제이션
def palindrome(i, j):
    if i == j or dp[i][j] >= 0:     # 길이가 1인 경우 or 이미 정해진 경우
        return dp[i][j]
    elif i + 1 == j:        # 길이가 2인 경우
        if arr[i] == arr[j]:
            dp[i][j] = 1
            return 1  # 팰린드롬 O
        else:
            dp[i][j] = 0
            return 0
    if arr[i] != arr[j]:
        dp[i][j] = 0
        return 0
    return palindrome(i + 1, j - 1)        # 재귀!


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(palindrome(a - 1, b - 1))