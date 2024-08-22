# N과 M (1) - DFS, 백트래킹
N, M = map(int, input().split())

graph = []

def dfs():
    if len(graph) == M:
        for i in range(M):
            print(graph[i], end=' ')
        print()
        return
    for i in range(1, N+1):
        if i not in graph:
            graph.append(i)
            dfs()
            graph.pop()
dfs()