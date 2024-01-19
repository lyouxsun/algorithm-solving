num = int(input())
arr = list(map(int, input().split()))

new_arr = [i**2 for i in arr]
for i in new_arr:
    print(i, end=' ')