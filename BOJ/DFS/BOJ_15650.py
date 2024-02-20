N, M = map(int, input().split())
g = []

def dfs():
    if len(g) == M:
        for i in range(M):
            print(g[i], end=' ')
        print()
        return
    for i in range(1, N+1):
        if len(g)==0 or g[-1] < i:
            g.append(i)
            dfs()
            g.pop()

dfs()