# 브루트 포스 - 3019번 - 테트리스
size, block = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


def block_1():
    global ans
    ans += size
    if size < 4:
        return
    for i in range(size - 3):
        if arr[i] == arr[i + 1] == arr[i + 2] == arr[i + 3]:
            ans += 1


def block_2():
    global ans
    if size < 2:
        return
    for i in range(size - 1):
        if arr[i] == arr[i + 1]:
            ans += 1


def block_3():
    global ans
    if size < 2:
        return
    for i in range(size - 1):
        if arr[i] == arr[i + 1] + 1:
            ans += 1
    for i in range(size - 2):
        if arr[i] == arr[i + 1] == arr[i + 2] - 1:
            ans += 1


def block_4():
    global ans
    if size < 2:
        return
    for i in range(size - 1):
        if arr[i] + 1 == arr[i + 1]:
            ans += 1
    for i in range(size - 2):
        if arr[i] - 1 == arr[i + 1] == arr[i + 2]:
            ans += 1


def block_5():
    global ans
    if size < 2:
        return
    for i in range(size - 1):
        if arr[i] + 1 == arr[i + 1]:
            ans += 1
        if arr[i] - 1 == arr[i + 1]:
            ans += 1
    for i in range(size - 2):
        if arr[i] == arr[i + 1] == arr[i + 2] or arr[i] == arr[i + 1] + 1 == arr[i + 2]:
            ans += 1


def block_6():
    global ans
    if size < 2:
        return
    for i in range(size - 1):
        if arr[i] - 2 == arr[i + 1] or arr[i] == arr[i + 1]:
            ans += 1
    for i in range(size - 2):
        if arr[i] + 1 == arr[i + 1] == arr[i + 2] or arr[i] == arr[i + 1] == arr[i + 2]:
            ans += 1


def block_7():
    global ans
    if size < 2:
        return
    for i in range(size - 1):
        if arr[i] == arr[i + 1] - 2 or arr[i] == arr[i + 1]:
            ans += 1
    for i in range(size - 2):
        if arr[i] == arr[i + 1] == arr[i + 2] + 1 or arr[i] == arr[i + 1] == arr[i + 2]:
            ans += 1


if block == 1:
    block_1()
elif block == 2:
    block_2()
elif block == 3:
    block_3()
elif block == 4:
    block_4()
elif block == 5:
    block_5()
elif block == 6:
    block_6()
elif block == 7:
    block_7()

print(ans)
