# BFS - 2251번 - 물통
## BFS가 가능한 이유 : 1.물통의 모든 상태를 고려해야 함 2.물을 나눠담는 조합의 경우의 수 = 200^3
from collections import deque
from copy import deepcopy
bucket = list(map(int, input().split()))        # 물통 A, B, C의 용량
result = [[0] * (bucket[1] + 1) for _ in range(bucket[0] + 1)]
# result[a][b] = 물통A에 a가 들어있고, 물통B에 b가 들어있을 때, 물통C에 들어있는 물의 양

_from = [0, 0, 1, 1, 2, 2]
_to = [1, 2, 0, 2, 0, 1]

q = deque()
q.append([0, 0, bucket[2]])
result[0][0] = 1
s = set()

while len(q) > 0:
    cur = q.popleft()
    if cur[0] == 0:
        s.add(bucket[2]-cur[1])
    for i in range(6):
        f, t = _from[i], _to[i]
        next = deepcopy(cur)
        if cur[f] < bucket[t]-cur[t]:     # case 1) 물을 주는 통(from)에 남아있는 걸 다 주기
            next[f] = 0
            next[t] += cur[f]
        else:                             # case 2) 물을 넣는 통(to)을 꽉 채우기
            next[f] -= bucket[t]-cur[t]
            next[t] = bucket[t]
        if result[next[0]][next[1]] == 0:
            result[next[0]][next[1]] = 1
            q.append(next)


ans = sorted(list(s))
for i in ans:
    print(i, end=' ')