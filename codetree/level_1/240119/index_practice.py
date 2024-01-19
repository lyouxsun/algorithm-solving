arr = list(map(int, input().split()))
index = 0
for i in range(len(arr)):
    if arr[i] % 3 == 0:
        index = i
        break
print(arr[index-1])

###
arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] % 3 == 0:
        print(arr[i-1])
        break