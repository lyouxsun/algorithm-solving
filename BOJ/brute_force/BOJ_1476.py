# 브루트 포스 - 1476번 - 날짜 계산

e, s, m = map(int, input().split())

# e+15*k == s+28*i == m + 19*j 인 k, i, j 를 구하는게 아니라 -> 같아지는 수를 구하면 됨.
# 1+15k == 16+28i == 16+19j
i = 0
while True:
    if (e + 15 * i - s) % 28 == 0 and (e + 15 * i - m) % 19 == 0:
        break
    i += 1
print(e + 15 * i)
