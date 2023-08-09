# 자료구조 - 25192번 - 인사성 밝은 곰곰이
import sys
input = sys.stdin.readline
N = int(input())
arr = set()
cnt = 0
for _ in range(N):
    string = input().strip()
    if string == 'ENTER':
        cnt += len(arr)
        arr = set()
    else:
        arr.add(string)
cnt += len(arr)
print(cnt)