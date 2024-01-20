n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        print(arr[line[1]-1], end=' ')
    elif line[0] == 2:
        if line[1] in arr:
            print(arr.index(line[1])+1, end=' ')
        else:
            print(0, end=' ')
    else:
        for i in range(line[1]-1, line[2]):
            print(arr[i], end = ' ')
    print()