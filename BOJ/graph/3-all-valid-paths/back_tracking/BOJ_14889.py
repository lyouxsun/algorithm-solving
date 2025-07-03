# 그래프 탐색 - 14889번 - 스타트와 링크
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]


def result(visited):
    start, link = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            if visited[i] == 1 and visited[j] == 1:
                start += arr[i][j] + arr[j][i]
                # print('start 더하기 : ', i, j , ' -> ', arr[i][j] ,  arr[j][i])
            if visited[i] == 0 and visited[j] == 0:
                link += arr[i][j] + arr[j][i]
                # print('link 더하기 : ', i, j, ' -> ', arr[i][j] ,  arr[j][i])
    return start, link


def dfs(level, index):  # level : 방문한 노드의 개수    # index : 지금 방문할 노드의 인덱스
    if level == n // 2:
        start, link = result(visited)
        # print(visited, 'start : ', start, 'link : ', link)
        global ans
        ans = min(ans, abs(start-link))
        return
    for i in range(index, n):       # index부터 시작이라는 조건이 없었더니 시간초과 발생!!!
        if visited[i] == 0:
            visited[i] = 1
            dfs(level + 1, i)
            visited[i] = 0


ans = float('inf')
dfs(0, 0)
print(ans)
