# DFS - 1914번 - 하노이 탑
import sys
sys.setrecursionlimit(10**6)
n = int(input())
strings = []
num = 0

# via : start -> end 로 가는 길에 경유하는 곳 (start, end가 아닌 나머지 하나를 의미함)
def hanoi(n, start, via, end):
    if n == 1:
        global num
        num += 1
        strings.append('%d %d' % (start, end))
    else:
        hanoi(n-1, start, end, via)
        num += 1
        strings.append('%d %d' % (start, end))
        hanoi(n-1, via, start, end)

if n <= 20:
    hanoi(n, 1, 2, 3)
    print(num)
    sys.stdout.write('\n'.join(strings))

# n이 20보다 클 때에는 재귀 없이 계산
else:
    ans = 1
    for _ in range(n-1):
        ans = ans * 2 + 1
    print(ans)