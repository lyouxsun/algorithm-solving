a, b = map(int, input().split())
arr=[]
arr.append(a)
arr.append(b)

for _ in range(8):
    arr.append((arr[-1] + arr[-2]) % 10)
    # if arr[-1]+arr[-2] >= 10:
    #     arr.append(arr[-1]+arr[-2]-10)
    # else:
    #     arr.append(arr[-1]+arr[-2])

for i in arr:
    print(i, end=' ')