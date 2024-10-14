# 문자열 - 1764번 - 듣보잡
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
heard = []
saw = []

for i in range(n):
    heard.append(input().strip())

for i in range(m):
    saw.append(input().strip())

heard.sort()
saw.sort()
ans = []
h, s = 0, 0

while True:
    if h >= n or s >= m:
        break
    if heard[h] == saw[s]:
        ans.append(saw[s])
        s += 1
    else:
        if heard[h] < saw[s]:
            h += 1
        else:
            s += 1


print(len(ans))
for i in ans:
    print(i)
