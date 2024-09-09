# 세그먼트 트리 - 10868번 - 최솟값
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]*n
ranges = []
for i in range(n):
    arr[i] = int(input())
for i in range(m):
    ranges.append(list(map(int, input().split())))

# === 세그먼트 트리 만들기 === #
# 1. 트리의 리프노드를 원본 데이터로 초기화
k = 0
while n > 2**k:
    k += 1
seg = [0]*2**k*2
for i in range(n):
    seg[2**k+i] = arr[i]
# print(seg)

# 2. 세그먼트 트리의 부모 노드 채우기
for idx in range(2**k-1, 0, -1):
    if seg[idx*2] == 0 and seg[idx*2+1] != 0:
        seg[idx] = seg[idx*2+1]
    elif seg[idx*2] != 0 and seg[idx*2+1] == 0:
        seg[idx] = seg[idx*2]
    else:
        seg[idx] = min(seg[idx*2], seg[idx*2+1])
# print(seg)

# 3. 질의값 구하기
for ran in ranges:
    start = ran[0] + 2**k -1
    end = ran[1] + 2**k -1
    # print(start, end)
    ans = float('inf')
    while start < end:
        if start % 2 == 1:
            ans = min(ans, seg[start])
            start += 1
        if end % 2 == 0:
            ans = min(ans, seg[end])
            end -= 1
        # print('중간, ', ans)
        start //= 2
        end //= 2
    if start == end:
        ans = min(ans, seg[start])
    print(ans)