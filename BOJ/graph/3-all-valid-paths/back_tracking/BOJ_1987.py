# 그래프 탐색 - 1987번 - 알파벳
## bfs인 줄 알았는데 백트래킹(dfs)이었다,,
# from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

dw = [-1, 1, 0, 0]
dh = [0, 0, -1, 1]
h, w = map(int, input().split())
alphabet = [list(input()) for _ in range(h)]
past = set()


def dfs(now_h, now_w, cnt):
    # print(alphabet[now_h][now_w], end=' -> ')
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        next_h = now_h + dh[i]
        next_w = now_w + dw[i]
        if (0 <= next_h < h) and (0 <= next_w < w):
            if alphabet[next_h][next_w] not in past:
                past.add(alphabet[next_h][next_w])
                dfs(next_h, next_w, cnt + 1)
                past.remove(alphabet[next_h][next_w])


past.add(alphabet[0][0])
ans = 0
dfs(0, 0, 1)
print(ans)
