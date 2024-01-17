arr = list(map(int, input().split()))
mark = 0
for i in range(len(arr)):
    if arr[i] == 0:
        mark = i
        break

if mark != 0:
    for i in arr[mark-1::-1]:
        print(i, end=' ')
else:
    for i in arr[::-1]:
        print(i, end=' ')