arr = [0 for _ in range(4)]
for _ in range(3):
    # a, b = tuple(input().split())
    a, b = input().split()
    if a == 'Y':
        if int(b) >= 37:
            arr[0] += 1
        else:
            arr[2] += 1
    else:
        if int(b) >= 37:
            arr[1] += 1
        else:
            arr[3] += 1
for i in arr:
    print(i, end=' ')
if arr[0] >= 2:
    print('E', end=' ')