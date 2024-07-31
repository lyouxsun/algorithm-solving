# 브루트 포스 - 16943번 - 숫자 재배치
from itertools import permutations

a, b = input().split()
if len(a) > len(b):
    print(-1)
    exit()

b = int(b)
ans = 0

for arr in permutations(a):
    # print(arr)
    if arr[0] == '0':
        continue
    tmp = int(''.join(arr))          # ('4', '1', '3', '2') 이 모양의 튜플을 네자리 정수로 변환
    # print(tmp)
    if ans < tmp < b:
        ans = tmp

if ans == 0:
    print(-1)
    exit()
else:
    print(ans)
