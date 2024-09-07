# 자료구조(세그먼트 트리) - 2357번 - 최솟값과 최댓값
import sys
input = sys.stdin.readline

def init_min_tree(node, start, end):
    if start == end:
        seg_min[node] = arr[start]
    else:
        mid = (start + end) // 2
        seg_min[node] = min(init_min_tree(node * 2, start, mid), init_min_tree(node * 2 + 1, mid + 1, end))
    return seg_min[node]

def init_max_tree(node, start, end):
    if start == end:
        seg_max[node] = arr[start]
    else:
        mid = (start + end) // 2
        seg_max[node] = max(init_max_tree(node * 2, start, mid), init_max_tree(node * 2 + 1, mid + 1, end))
    return seg_max[node]

def query_min(node, start, end, left, right):
    if left > end or right < start:
        return float('inf')
    if left <= start and end <= right:
        return seg_min[node]
    mid = (start + end) // 2
    return min(query_min(node * 2, start, mid, left, right), query_min(node * 2 + 1, mid + 1, end, left, right))

def query_max(node, start, end, left, right):
    if left > end or right < start:
        return -float('inf')
    if left <= start and end <= right:
        return seg_max[node]
    mid = (start + end) // 2
    return max(query_max(node * 2, start, mid, left, right), query_max(node * 2 + 1, mid + 1, end, left, right))

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
ranges = [list(map(int, input().split())) for _ in range(m)]

size = 2 ** (n - 1).bit_length()
seg_min = [float('inf')] * (2 * size)
seg_max = [-float('inf')] * (2 * size)

init_min_tree(1, 0, n - 1)
init_max_tree(1, 0, n - 1)

for ran in ranges:
    start, end = ran[0] - 1, ran[1] - 1
    min_val = query_min(1, 0, n - 1, start, end)
    max_val = query_max(1, 0, n - 1, start, end)
    print(min_val, max_val)
