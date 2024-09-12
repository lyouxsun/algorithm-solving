# 세그먼트 트리 - 2268번 - 수들의 합 7
import sys
input = sys.stdin.readline

functions = []
n, m = map(int, input().split())
for i in range(m):
    functions.append(list(map(int, input().split())))
k = 0
while n > 2**k:
    k += 1
seg = [0]*2**k*2

def Sum(start, end):
    start += 2**k-1
    end += 2**k-1
    ans = 0
    while start <= end:
        if start % 2== 1:
            ans += seg[start]
            start += 1
        if end % 2 == 0:
            ans += seg[end]
            end -=1
        start //=2
        end //= 2
    print(ans)

def Modify(index, new):
    index += 2**k-1
    old = seg[index]
    # seg[index] = new
    while index > 0:
        seg[index] += -old+new
        index //= 2

for (f, i, j) in functions:
    # print(func)
    if f == 0:        # Sum 함수
        if i > j:
            Sum(j, i)
        else:
            Sum(i, j)
    else:
        Modify(i, j)
    # print(seg)
    # print()

# 3 5
# 1 1 3
# 1 3 2
# 1 3 5
# 1 2 4
# 0 1 2
# 답 : 7