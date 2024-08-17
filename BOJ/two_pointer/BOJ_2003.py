# 투포인터 - 2003번 - 수들의 합2
n, m = map(int, input().split())
s = list(map(int, input().split()))
for i in range(1, n):
    s[i] = s[i-1]+s[i]
s.insert(0, 0)
start, end, cnt = 0, 0, 0
while end <=n:
    if s[end] - s[start] == m:
        cnt += 1
        end += 1
    elif s[end] - s[start] > m:
        start += 1
    else:
        end +=1
print(cnt)