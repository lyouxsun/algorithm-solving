cycle = int(input())
for _ in range(cycle):
    a, b = map(int, input().split())
    cnt = 1
    for i in range(a, b+1):
        cnt *= i
    print(cnt)