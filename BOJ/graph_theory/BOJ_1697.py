# BFS로 풀래..ㅠ
import sys
from collections import deque
input = sys.stdin.readline()

def bfs():
    q = deque()
    q.append(N)
    while q:
        num = q.popleft()
        if K == num:
            print(visited[K])
            return
        for i in (num-1, num+1, num*2):
            if (0 <= i < K * 2) and visited[i] == 0:   # (i not in q)를 visited[i]==0 으로 바꿨다고 시간초과가 해결된다고?
                visited[i] = visited[num]+1
                q.append(i)

N, K = map(int, input.split())
if K <= N:
    print(N-K)
    exit(0)
visited = [0] * (K * 2)
bfs()