# 세그먼트 트리 - 14427번 - 수열과 쿼리 15
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
query = []
for _ in range(m):
    query.append(list(map(int, input().split())))

k = 0
while n >= 2**k:
    k += 1
seg = [[float('inf'), 0] for i in range(2**k*2)]
for i in range(n):
    seg[i + 2**k] = [arr[i], i+1]
for i in range(2**k-1, 0, -1):
    if seg[i*2][0] <= seg[i*2+1][0]:
        seg[i] = seg[i*2]
    else:
        seg[i] = seg[i*2+1]

def seg_change(idx, new):
    idx += 2**k-1
    seg[idx][0] = new
    idx //= 2
    while idx > 0:
        if seg[idx * 2][0] <= seg[idx * 2 + 1][0]:
            seg[idx] = seg[idx * 2]
        else:
            seg[idx] = seg[idx * 2 + 1]
        idx //= 2

for i in query:
    if i[0] == 2:
        print(seg[1][1])
    else:
        seg_change(i[1], i[2])
        # print(seg)