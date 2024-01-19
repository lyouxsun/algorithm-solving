# v1. append 이용하기
arr = [0, 1, 1]
for i in range(3, 11):
    arr.append(arr[-1] + arr[-2])

# v2.
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr[1] = arr[2] = 1
for i in range(3, 11):
    arr[i] = arr[i - 1] + arr[i - 2]

# v3. 배열 이용하지 않고
pp, p = 1, 1
for _ in range(3, 11):
    pp, p = p, pp + p