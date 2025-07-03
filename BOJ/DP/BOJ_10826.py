# dp - 10826번 - 피보나치 수 4
import sys
input = sys.stdin.readline

n = int(input())
fib = [-1] * (n+2)      # +2를 해줘야 n=0인 경우에도 indexError가 발생하지 않는다
fib[0] = 0
fib[1] = 1
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[n])