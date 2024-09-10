# 세그먼트 트리 - 11505번 - 구간 곱 구하기
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0] * n
cond = []
for i in range(n):
    arr[i] = int(input())
for i in range(m + k):
    cond.append(list(map(int, input().split())))


def seg_change(index, new):
    global s
    index += 2 ** s - 1
    seg[index] = new
    index //= 2
    while index > 0:
        seg[index] = seg[index * 2] * seg[index * 2 + 1] % 1000000007
        index //= 2
    # print("변경 후=", seg)


def seg_result(start, end):
    global s
    start += 2 ** s - 1
    end += 2 ** s - 1
    ans = 1
    while start <= end:
        if start % 2 == 1:
            ans *= seg[start]
            start += 1
        if end % 2 == 0:
            ans *= seg[end]
            end -= 1
        ans %= 1000000007
        start //= 2
        end //= 2
    print(ans % 1000000007)


# == 세그먼트 트리 만들기 == #
# 1. 리프노드 초기화
s = 0
while n > 2 ** s:
    s += 1
seg = [1] * 2 ** s * 2
for i in range(n):
    seg[i + 2 ** s] = arr[i] % 1000000007

# 2. 부모노드 채우기
for idx in range(2 ** s - 1, 0, -1):
    seg[idx] = seg[idx * 2] * seg[idx * 2 + 1] % 1000000007
# print(seg)

# 3. 질의값 구하기
for c in cond:
    if c[0] == 1:  # 데이터 변경
        seg_change(c[1], c[2])
    else:
        seg_result(c[1], c[2])
