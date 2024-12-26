# 분할 정복 - 1074번 - Z
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
# print(arr)
# 1. 크게 네 덩이로 나누고 그중에 어느 파트인지 확인, 그 파트가 몇부터 몇까지인지 확인
# 2. 그 파트 안에서 네 덩이 중 어디인지 확인
# 3. 반복

def where(n):
    if 0 <= r < 2 ** (n - 1):
        if 0 <= c < 2 ** (n - 1):
            return 1
        return 2
    else:
        if 0 <= c < 2 ** (n - 1):
            return 3
    return 4


part, n = 0, N
ans = 0
while True:
    if n == 0:
        break
    part = where(n)
    # print('part=', part)
    n -= 1
    # print('(2 ** n)=', (2 ** n))
    ans += (2 ** n) ** 2 * (part - 1)
    # print('ans=', ans)
    if part == 2:
        c -= 2 ** n
    elif part == 3:
        r -= 2 ** n
    elif part == 4:
        c -= 2 ** n
        r -= 2 ** n

print(ans)
