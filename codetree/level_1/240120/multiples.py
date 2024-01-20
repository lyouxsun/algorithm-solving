num = int(input())
cnt = 0
i = 1

while True:
    if cnt == 2:
        break
    if num * i % 5 == 0:
        cnt += 1
    print(num * i, end = ' ')
    i += 1