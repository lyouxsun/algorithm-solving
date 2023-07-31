# 그리디 알고리즘 - 12904번 - A와 B
import sys
input = sys.stdin.readline
before = input().strip()
after = list(input().strip())
for i in range(len(after)-len(before)):
    if after[-1]=='A':
        del after[-1]
    elif after[-1]=='B':
        del after[-1]
        after.reverse()
if str(''.join(after)) == before:
    print("1")
else:
    print("0")