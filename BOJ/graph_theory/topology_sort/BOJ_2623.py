# 위상정렬 - 2623번 - 음악프로그램
## 인접 리스트에 내가 가리키는, 나 다음에 오는 1개의 노드만 저장한다. + 나를 가리키는 노드의 수도 카운트한다.
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0, []] for i in range(n + 1)]

for j in range(m):
    l = list(map(int, input().split()))
    length = l.pop(0)
    now, next = l[0], 0
    for i in range(length-1):
        next = l[i+1]
        arr[now][1].append(next)
        arr[next][0] += 1
        now = next


q = deque()
for i in range(1, n+1):
    if arr[i][0] == 0:
        q.append(i)

ans = []
cnt = 0
while q:
    # print(q, ans)
    now = q.popleft()
    ans.append(now)
    cnt += 1
    for next in arr[now][1]:
        arr[next][0] -= 1
        if arr[next][0] == 0:
            q.append(next)

# print(ans)

if cnt != n:
    print(0)
else:
    for i in ans:
        print(i)

# 사이클 예제
# 3 1
# 4 1 2 3 1
# answer : 0
#
# 4 2
# 3 1 2 3
# 3 3 4 2
# answer : 0
# 2 2
# 1 1
# 1 1
