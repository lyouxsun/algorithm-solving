arr = list(map(int, input().split()))
cnt, sum = 0, 0
for i in arr:
    if i!=0:
        sum += i
        cnt += 1
    else:
        break
print(f'{sum} {sum/cnt:.1f}')