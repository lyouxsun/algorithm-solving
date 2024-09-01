# BFS - 13549번 - 숨바꼭질
from collections import deque

me, target = map(int, input().split())
if me > target:
    print(me - target)
    exit()
elif me == target:
    print(0)
    exit()
# me < target인 경우만 고려하기!
visited = [float('inf')] * (target * 2 + 1)

q = deque()
visited[me] = 0
q.append([me, 0])
ans = float('inf')

while q:
    # print(q)
    now, cnt = q.popleft()
    if now == target:
        visited[now] = min(visited[now], cnt)
        # print(cnt)
        continue
    if now > target * 2:
        continue
    if now * 2 <= target * 2 and visited[now * 2] > cnt:
        visited[now * 2] = cnt
        q.append([now * 2, cnt])
    if now + 1 <= target * 2 and visited[now + 1] > cnt + 1:
        visited[now + 1] = cnt + 1
        q.append([now + 1, cnt + 1])
    if now - 1 >= 0 and visited[now - 1] > cnt + 1:
        visited[now - 1] = cnt + 1
        q.append([now - 1, cnt + 1])

print(visited[target])
