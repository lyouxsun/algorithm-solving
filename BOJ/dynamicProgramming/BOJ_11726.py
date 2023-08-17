# 다이나믹 프로그래밍 - 11726번 - 2*n 타일링
import sys
input = sys.stdin.readline
N = int(input())
answer = [0 for i in range(N+2)]
answer[1]=1
answer[2]=2
for i in range(3, N+1):
    answer[i] = answer[i-1]+answer[i-2]
print(answer[N]%10007)