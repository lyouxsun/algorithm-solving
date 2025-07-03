# 11404번 - 플로이드 워셜 - 플로이드
n = int(input())
m = int(input())

# 처음에 테이블을 초기화 할 때에는 모든 값을 inf로 해줘야 한다!
# arr[i][j] : i노드에서 j노드로 가는데 필요한 최소 비용을 저장하는 테이블
arr = [[float('inf') for _ in range(n)] for _ in range(n)]
for _ in range(m):
    start, end, weight = map(int, input().split())
    if arr[start - 1][end - 1] != 0:
        arr[start - 1][end - 1] = min(arr[start - 1][end - 1], weight)
        continue
    arr[start - 1][end - 1] = weight
# print(arr)

# s에서 e로 가려할 때, s->e 와 s->stop->e 중 더 적은 비용을 arr에 저장
for stop in range(n):
    arr[stop][stop] = 0
    for s in range(n):
        for e in range(n):
            if arr[s][stop] != 0 and arr[stop][e] != 0:
                arr[s][e] = min(arr[s][e], arr[s][stop] + arr[stop][e])

# print(arr)
for i in range(n):
    for j in range(n):
        if arr[i][j] == float('inf'):
            arr[i][j] = 0
        print(arr[i][j], end=' ')
    print()
