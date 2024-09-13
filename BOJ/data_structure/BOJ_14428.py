# 세그먼트 트리 - 14428번 - 수열과 쿼리 16
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
func = []
for _ in range(m):
    func.append(list(map(int, input().split())))
k = 0
while n > 2 ** k:
    k += 1
seg = [(float('inf'), -1)] * 2 ** k * 2
for i in range(n):
    seg[i + 2 ** k] = (arr[i], i)
for i in range(2 ** k - 1, 0, -1):
    right = seg[i*2]
    left = seg[i*2+1]
    if right[0] <= left[0]:
        seg[i] = right
    else:
        seg[i] = left


# print(seg)

def change_seg(index, new):
    index += 2 ** k - 1
    seg[index] = (new, index-2 ** k)
    index //= 2
    while index > 0:
        right = seg[index * 2]
        left = seg[index * 2 + 1]
        if right[0] <= left[0]:
            seg[index] = right
        else:
            seg[index] = left
        index //= 2


def min_seg(start, end):
    start += 2 ** k - 1
    end += 2 ** k - 1
    # print('start=', start, ', end=', end)
    ans = float('inf')
    ans_idx = float('inf')
    while start <= end:
        if ans == seg[start][0]:
            ans_idx = min(ans_idx, seg[start][1])
        if ans == seg[end][0]:
            ans_idx = min(ans_idx, seg[end][1])
        if start % 2 == 1:
            if ans > seg[start][0]:
                ans = seg[start][0]
                ans_idx = seg[start][1]
            start += 1
        if end % 2 == 0:
            if ans > seg[end][0]:
                ans = seg[end][0]
                ans_idx = seg[end][1]
            end -= 1
        start //= 2
        end //= 2
        # print('ans=%d, ans_idx=%d'%(ans, ans_idx))
    # print('최솟값= ', ans)
    print(ans_idx+1)


for (a, b, c) in func:
    if a == 1:
        change_seg(b, c)
    else:
        # print(seg)
        min_seg(b, c)

# 5
# 1 1 1 1 1
# 1
# 2 1 3
# 답 : 1