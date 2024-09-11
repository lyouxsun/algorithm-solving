# 세그먼트 트리 - 1275번 - 커피숍2
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
turns = []
for _ in range(q):
    turns.append(list(map(int, input().split())))
k = 0
while n > 2 ** k:
    k += 1
seg = [0] * 2 ** k * 2
for i in range(n):
    seg[2 ** k + i] = arr[i]
for idx in range(2 ** k - 1, 0, -1):
    seg[idx] = seg[idx * 2] + seg[idx * 2 + 1]
# print(seg)

def seg_sum(start, end):
    start += 2 ** k - 1
    end += 2 ** k - 1
    ans = 0
    while start <= end:
        if start % 2 == 1:
            ans += seg[start]
            start += 1
        if end % 2 == 0:
            ans += seg[end]
            end -= 1
        start //= 2
        end //= 2
    print(ans)


def seg_change(index, new):
    index += 2 ** k - 1
    old = seg[index]
    while index > 0:
        seg[index] += -old + new
        index //= 2


for i in range(q):
    (x, y, a, b) = turns[i]
    if y > x:
        seg_sum(x, y)
    else:
        seg_sum(y, x)
    seg_change(a, b)
