# 스택 - 28278번 - 스택2
import sys
input = sys.stdin.readline

stack = []
n = int(input())

for _ in range(n):
    m = input().split()
    # print(m)
    if  m[0] == '1':
        stack.append(int(m[1]))
    elif m[0] == '2':
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    elif m[0] == '3':
        print(len(stack))
    elif m[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif m[0] == '5':
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)
