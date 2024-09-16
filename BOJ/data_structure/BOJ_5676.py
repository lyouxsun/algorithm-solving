# 세그먼트 트리 - 5676번 - 음주 코딩
import sys
input = sys.stdin.readline


def change(seg, idx, new):
    idx += 2 ** k - 1
    seg[idx] = new
    idx //= 2
    while idx > 0:
        seg[idx] = seg[idx * 2] * seg[idx * 2 + 1]
        idx //= 2
    # print(seg)


def multiple(seg, start, end):
    start += 2 ** k - 1
    end += 2 ** k - 1
    ans = 1
    while start <= end:
        if start % 2 == 1:
            ans *= seg[start]
            start += 1
        if end % 2 == 0:
            ans *= seg[end]
            end -= 1
        start //= 2
        end //= 2
    # print('ans =', ans)
    if ans > 0:
        print('+', end='')
    elif ans < 0:
        print('-', end='')
    else:
        print('0', end='')


while True:
    try:
        n, m = map(int, input().split())
    except (ValueError, EOFError):
        exit()
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] > 0:
            arr[i] = 1
        elif arr[i] < 0:
            arr[i] = -1
    func = []
    for _ in range(m):
        func.append(list(input().split()))
    k = 0
    while n > 2 ** k:
        k += 1
    seg = [1] * 2 ** k * 2
    for i in range(n):
        seg[i + 2 ** k] = arr[i]
    for i in range(2 ** k - 1, 0, -1):
        seg[i] = seg[i * 2] * seg[i * 2 + 1]
    for (a, b, c) in func:
        if a == 'C':
            if int(c) > 0:
                c = 1
            elif int(c) < 0:
                c = -1
            else:
                c = 0
            change(seg, int(b), c)
        else:
            multiple(seg, int(b), int(c))
    print()
