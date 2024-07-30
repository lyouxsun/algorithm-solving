# 브루트 포스 - 16922번 - 로마 숫자 만들기
## (1, 5, 10, 50) 의 합으로 만들 수 있는 숫자의 개수 구하기
## 식1. a+b+c+d = (사용할 수 있는 숫자 개수)
## 식2. a+5b+10c+50d = (만들 수 있는 숫자)
## Q. 4중 for문,, 최선일까..?

# 모든 수를 만들어보는 방식 = 2^40 = 몇조 (x)
# 같은 수로 구성되어 있고 순서만 다른 수 = 1가지로 취급 -> 이 경우에 모든 수를 구할 필요 없이 하나만 있으면 된다.

n = int(input())
sum_arr = [0] * (n * 50 + 1)

for a in range(n + 1):
    for b in range(n - a + 1):
        for c in range(n - a - b + 1):
            for d in range(n - a - b - c + 1):
                if a == b == c == d == 0 or a+b+c+d != n:
                    continue
                if n - a < 0 or n - a - b < 0 or n - a - b - c < 0:
                    continue
                else:
                    # print(a, b, c, d)
                    # print(1 * a + 5 * b + 10 * c + 50 * d)
                    sum_arr[1 * a + 5 * b + 10 * c + 50 * d] = 1

print(sum(sum_arr))
