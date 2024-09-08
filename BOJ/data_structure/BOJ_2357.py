# 자료구조(세그먼트 트리) - 2357번 - 최솟값과 최댓값
## n, m -> 구간의 합/차 또는 최댓값/최솟값을 구할 때에는 세그먼트 트리를 사용한다.
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr, ranges = [], []
for _ in range(n):
    arr.append(int(input()))
for _ in range(m):
    ranges.append(list(map(int, input().split())))

# 1. 최댓값/최솟값 세그먼트 초기화
k = 0
while 2 ** k < n:  # 2**k >= n 인 k 찾기
    k += 1
max_seg, min_seg = [0] * 2 ** k * 2, [0] * 2 ** k * 2
for i in range(n):
    max_seg[2 ** k + i] = arr[i]
    min_seg[2 ** k + i] = arr[i]
# print(max_seg)

## 2-1. 최댓값 세그먼트 트리의 부모노드 채우기
for idx in range(2 ** k - 1, 0, -1):
    max_seg[idx] = max(max_seg[2 * idx], max_seg[2 * idx + 1])
# print('max_seg=', max_seg)

## 2-2. 최솟값 세그먼트 트리의 부모노드 채우기
for idx in range(2 ** k - 1, 0, -1):
    if min_seg[2 * idx] == 0 and min_seg[2 * idx + 1] == 0:
        continue
    if min_seg[2 * idx] == 0:
        min_seg[idx] = min_seg[2 * idx + 1]
    if min_seg[2 * idx + 1] == 0:
        min_seg[idx] = min_seg[2 * idx]
    else:
        min_seg[idx] = min(min_seg[2 * idx], min_seg[2 * idx + 1])


# print('min_seg=', min_seg)

# 3. 범위에 따른 최솟값과 최댓값 출력하기
def segment_max_min(start, end):
    global k
    # 인덱스 바꾸기
    s = start + 2 ** k - 1
    e = end + 2 ** k - 1
    # print('[변경된 index] start=%d, end=%d'%(start, end))

    # 최솟값 출력
    ans = float('inf')
    while s <= e:
        if s % 2 == 1:
            ans = min(ans, min_seg[s])
            s += 1
        if e % 2 == 0:
            ans = min(ans, min_seg[e])
            e -= 1
        s //= 2
        e //= 2
    if s == e:
        ans = min(ans, min_seg[s])
    print(ans, end=' ')

    # 최댓값 출력
    s = start + 2 ** k - 1
    e = end + 2 ** k - 1
    ans = 0
    while s <= e:
        # print('ans=',ans)
        if s % 2 == 1:
            ans = max(ans, max_seg[s])
            s += 1
        if e % 2 == 0:
            ans = max(ans, max_seg[e])
            e -= 1
        s //= 2
        e //= 2
    # print('max_seg[start]=%d, max_seg[end]=%d'%(max_seg[s], max_seg[e]))
    # print('start=%d, end=%d'%(s, e))
    if s == e:
        ans = max(ans, max_seg[s])
    print(ans)


for ran in ranges:
    segment_max_min(ran[0], ran[1])

# 5 1
# 1
# 2
# 3
# 4
# 5
# 1 3
