# dp - 2784번 - 피보나치 수 2
import sys
input = sys.stdin.readline

n = int(input())
fib = [-1] * (n+1)
fib[1] = 1
fib[0] = 0
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[n])