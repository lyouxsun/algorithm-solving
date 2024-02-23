cycle = int(input())
arr = [list(map(int, input().split())) for _ in range(cycle) ]

for i in range(cycle):
    cnt = 1
    for j in range(cycle):
        if i==j:
            continue
        else:
            if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
                cnt+=1
    print(cnt, end=' ') 
