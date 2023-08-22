# 다이나믹 프로그래밍 - 10844번 - 쉬운 계단 수
import sys
input = sys.stdin.readline
N = int(input())
answer = 9 * 2**(N-1)
if N > 1:
    answer -= 2**(N-2)
    for i in range(1, N-1):
        answer -= 2**i
print(answer)

'''
1 : 9
2 : 17
3 : 32
4 : 61
5 : 116
6 : 222
7 : 424
50 : 894685264
95 : 989279221
'''