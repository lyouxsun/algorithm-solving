# 스택 - 1725번 - 히스토그램
# [스택] 1. 직사각형의 높이를 고정시키는 풀이
## [meet in the middle] 2. 분할 정복을 이용한 풀이1
## [세그먼트 트리] 3. 분할 정복을 이용한 풀이2 (자료구조를 이용)
n = int(input())
histo = list(int(input()) for _ in range(n))
stack = [0]

# print(stack)

ans = 0
for i in range(n):
    # print('[while 전] i=', i, 'stack=', stack)
    left = i
    while len(stack)> 0 and histo[stack[-1]] > histo[i]:
        height = histo[stack.pop()]
        width = i
        if len(stack) !=0:
            width = i - stack[-1]-1
        ans = max(ans, height*width)
    stack.append(i)
    while len(stack)> 0:
        height = histo[stack.pop()]
        width = n
        if len(stack) !=0:
            width = n - stack[-1]-1
        ans = max(ans, height*width)

    # print('[while 후] i=', i, 'stack=', stack)
print(ans)

# 10
# 1
# 2
# 3
# 4
# 5
# 10
# 7
# 8
# 9
# 10
# 답 : 35