num = int(input())
for i in range(1, num+1):
    if i == 2:
        print(i, end=' ')
        continue
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i-1:
            print(i, end=' ')