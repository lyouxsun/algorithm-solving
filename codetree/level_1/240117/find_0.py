arr = list(map(int, input().split()))
sum, cnt = 0, 0

for i in arr:
    if i == 0:
        break
    if i%2 == 0:
        sum += i
        cnt += 1
print(f'{cnt} {sum}')