# dfs - 1967번 - 트리의 지름
## 1. 루트 노드인 1번 노드로부터 가장 멀리 떨어져있는 노드를 찾는다.
## 2. 1번에서 찾은 노드로부터 가장 멀리 떨어져있는 노드를 찾는다.
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for i in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

def distance(now, d):
    for (next, weight) in tree[now]:
        if d[next] == -1:
            d[next] = d[now] + weight
            distance(next, d)


# 1. 루트노드에서 다른 점들까지의 거리를 구한다.
d = [-1] * (n + 1)
d[1] = 0
distance(1, d)
max_value, idx = 0, -1
for i in range(1, n+1):
    if max_value < d[i]:
        max_value = d[i]
        idx = i

# 2. 1번에서 찾은 노드로부터 다른 점들까지의 거리를 구한다.
d = [-1] * (n + 1)
d[idx] = 0
distance(idx, d)
print(max(d))

