# 자료구조 (세그먼트 트리) - 2042번 - 구간 합 구하기
## 그냥 구간합 -> prefix sum / 계속 업데이트 될 때의 구간합 -> 세그먼트 트리
n, m, l = map(int, input().split())
data = [0] * n
for i in range(n):
    data[i] = int(input())

# === 세그먼트 트리 만들기 ===
## 1. 세그먼트 트리 크기 정하기
k = 0
while 2 ** k < n:
    k += 1

## 2. 세그먼트 트리 초기화하기
seg = [0]*2**k*2
for i in range(n):
    seg[2**k+i] = data[i]
# print(seg)

## 3. 트리의 부모 노드 채우기
for idx in range(2**k-1, 1, -1):
    seg[idx] = seg[idx*2] + seg[idx*2+1]
# print(seg)
# =======================

def segment_change(k, b, c):
    idx = 2**k+b-1
    old = seg[idx]

    # 부모노드를 타고 올라가며 변경된 값만 바꿔주기
    while idx >= 1:
        seg[idx] -= old
        seg[idx] += c
        idx //= 2
    # print('변경 후 segment tree =', seg)

def segment_sum(k, start, end):
    ans = 0
    # print('[인덱스 변경 전] %d부터 %d까지의 구간 합' % (start, end))
    start += 2**k-1
    end += 2**k-1
    # print('[인덱스 변경 후] %d부터 %d까지의 구간 합' % (start, end))

    while start < end:
        if start %2 == 1:
            ans += seg[start]
            # print('[start] ans에 독립 노드 더하기 +%d (idx=%d) => ans=%d'%(seg[start], start, ans))
            start += 1
        if end % 2 == 0:
            ans += seg[end]
            # print('[end] ans에 독립 노드 더하기 +%d (idx=%d) => ans=%d'%(seg[end], end, ans))
            end -= 1
        start //= 2
        end //=2
    if start == end:        # start!=end 인 경우에는 이미 start > end 로 엇갈린 상태이므로 ans에 이미 더해져 있음!
        ans += seg[start]
    # print('구간 합 = %d' %(ans))
    # print()
    return ans

# a가 1인 경우 = 데이터 변경 : b번째 수를 c로 바꾸기
# a가 2인 경우 = 구간합 구하기 : b번째 수부터 c번째 수까지의 합 출력하기
# print('m=',m,', l=',l)
for i in range(m + l):
    a, b, c = map(int, input().split())
    # 데이터 변경
    if a == 1:
        segment_change(k, b, c)
    # 구간합 구하기
    if a == 2:
        # segment_sum(k, b, c)
        print(segment_sum(k, b, c))


# 5 2 2
# 1
# 2
# 3
# 4
# 5
# 1 3 6
# 2 2 5
# 1 5 2
# 2 3 3

# 1 2 1
# 1
# 1 1 2
# 1 1 2
# 2 1 1