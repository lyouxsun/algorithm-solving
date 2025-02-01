# 해시를 사용한 집합과 맵 - 9375번 - 패션왕 신해빈
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    d = dict()
    cate = set()
    for _ in range(n):
        wear, category = input().split()
        cate.add(category)
        if category not in d:
            d[category] = set()
        d[category].add(wear)
    ans = 1
    for c in list(cate):
        ans *= (len(d[c]) + 1)
    ans -= 1
    print(ans)
