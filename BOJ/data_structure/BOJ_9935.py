# 자료구조(스택) - 9935번 - 문자열 폭발
import sys
input = sys.stdin.readline

arr = list(input().strip())
n = len(arr)
bomb = list(input().strip())
b = len(bomb)

# print(arr)
# print(bomb)

exp = []
i = 0
while i < n:
    exp.append(arr[i])
    if len(exp) >= b and exp[-b:] == bomb:
        del exp[-b:]
    i += 1
    # print(exp)

if len(exp) == 0:
    print('FRULA')
else:
    print(''.join(exp))
