# 11725번 - 그래프 탐색 - 트리의 부모 찾기
## BFS
# 매번 visited를 초기화하는 방법은 무조건 시간초과 발생!!!
# -> visited에 자신의 부모 번호를 저장했다가 한번에 출력하는 방식ㄱㄱ

from collections import deque

n = int(input())
q = deque()
arr = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    # print(arr)


def bfs():
    visited[0] = 1
    visited[1] = 1
    for i in arr[1]:
        visited[i] = 1
        q.append(i)

    while 0 in visited:
        next = q.popleft()
        for i in arr[next]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = next


bfs()
for i in range(2, n + 1):
    print(visited[i])
