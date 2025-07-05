import sys
input = sys.stdin.readline

N = list(input().strip())
result = 0
mult = 1

for i in range(len(N)):
    if N[i] == '*':
        if i % 2 == 1:
            mult = 3
    else:
        x = int(N[i])
        if i % 2 == 0:
            result += x
        else:
            result += 3 * x

for i in range(10):
    if (result + mult*i ) % 10 == 0:
        print(i)
        break