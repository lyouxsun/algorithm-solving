n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
before = -1
for i in range(m):
    if i%2 == 0:
        for j in range(n):
            arr[j][i] = before + 1
            before = arr[j][i]
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] = before + 1
            before = arr[j][i]
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()