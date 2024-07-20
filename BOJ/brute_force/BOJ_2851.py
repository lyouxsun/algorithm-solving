# 부르트 포스 - 2851번 - 슈퍼 마리오
ans = 0
for i in range(10):
    before = ans
    ans += int(input())
    if ans > 100:
        if (ans - 100) <= (100 - before):
            print(ans)
        else:
            print(before)
        break
    if i == 9:
        print(ans)