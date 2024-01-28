n = int(input())
start = 1
for j in range(n):
    for i in range(n):
        print(start+i*n, end=' ')
    start+=1
    print()