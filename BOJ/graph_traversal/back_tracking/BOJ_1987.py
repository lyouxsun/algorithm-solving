# 그래프 탐색 - 1987번 - 알파벳
## bfs인 줄 알았는데 백트래킹(dfs)이었다,,
from collections import deque

dw = [-1, 1, 0, 0]
dh = [0, 0, -1, 1]
h, w = map(int, input().split())
alphabet = [list(input()) for _ in range(h)]
past = set()


def bfs():
    q = deque()
    q.append([0, 0])
    past.add(alphabet[0][0])
    cnt = 1

    while q:
        now_h, now_w = q.popleft()
        for i in range(4):
            nh = now_h + dh[i]
            nw = now_w + dw[i]
            if (0 <= nh < h) and (0 <= nw < w):
                if alphabet[nh][nw] not in past:
                    past.add(alphabet[nh][nw])
                    q.append([nh, nw])
                    cnt += 1
                    # print('alphabet[', nh, '][', nw, '] = ', alphabet[nh][nw])
    return cnt


print(bfs())
