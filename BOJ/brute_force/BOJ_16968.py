# 브루트 포스 - 16968번 - 차량 번호판 1

str = input()

CHAR = 26
NUM = 10
ans = 1
for i in range(len(str)):
    if str[i] == 'c':
        if i > 0 and str[i - 1] == 'c':
            ans *= (CHAR - 1)
        else:
            ans *= CHAR
    else:
        if i > 0 and str[i - 1] == 'd':
            ans *= (NUM - 1)
        else:
            ans *= NUM
print(ans)
