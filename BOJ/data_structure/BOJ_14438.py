# 세그먼트 트리 - 14438번 - 수열과 쿼리 17
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
func = []
for i in range(m):
    func.append(list(map(int, input().split())))
k = 0
while n > 2 ** k:
    k += 1
seg = [float('inf')] * 2 ** k * 2
for i in range(n):
    seg[i + 2 ** k] = arr[i]
for i in range(2 ** k - 1, 0, -1):
    seg[i] = min(seg[2 * i], seg[2 * i + 1])


# print(seg)

def seg_change(index, new):
    index += 2 ** k - 1
    seg[index] = new
    index //= 2
    while index > 0:
        seg[index] = min(seg[2 * index], seg[2 * index + 1])
        index //= 2


def seg_print(start, end):
    start += 2 ** k - 1
    end += 2 ** k - 1
    # print('start=', start, ', end=', end)
    ans = float('inf')
    while start <= end:
        if start % 2 == 1:
            ans = min(ans, seg[start])
            start += 1
        if end % 2 == 0:
            ans = min(ans, seg[end])
            end -= 1
        start //= 2
        end //= 2
    print(ans)


for (a, b, c) in func:
    # print(a, b, c)
    if a == 1:
        seg_change(b, c)
    else:
        seg_print(b, c)
