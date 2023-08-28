# 다이나믹 프로그래밍 - 10844번 - 쉬운 계단 수
import sys
input = sys.stdin.readline
N = int(input())
dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, N+1):
    for j in range(10):
        if j==0:
            dp[i][j] = dp[i-1][1]
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# print(dp)
answer = sum(dp[N]) % 1000000000
# 2차원 배열은 전체 sum으로 합하는게 안되고 행별로 합하는 것만 되는것같음
print(answer)


'''
1 : 9    -1
2 : 17   -1
3 : 32   -2 
4 : 61   -3
5 : 116   -6
6 : 222   -10
7 : 424   -20
50 : 894685264
95 : 989279221
'''