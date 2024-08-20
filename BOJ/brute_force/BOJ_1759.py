# 브루트 포스 - 1759번 - 암호 만들기
from itertools import combinations

l, c = map(int, input().split())
arr = list(input().split())
vowel = ['a', 'e', 'i', 'o','u']

comb = combinations(arr, l)
ans = set()
for array in comb:
    cnt_v = 0
    for i in array:
        if i in vowel:
            cnt_v += 1
    if cnt_v < 1 or l-cnt_v < 2:
        continue
    else:
        tmp = ''.join(sorted(array))
        ans.add(tmp)

a = sorted(list(ans))
for i in a:
    print(i)



