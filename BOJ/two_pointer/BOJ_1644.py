# 투포인트 - 1644번 - 소수의 연속합
# 소수 -> 에라토스테네스의 체
## 200만까지 구하면 됨

## 소수만 남기고 나머지 수는 다 0으로 만들기
# 1. 배열 생성 & 초기화
n = int(input())
arr = [i for i in range(n + 1)]
cnt = 0

# 2. 특정 수의 배수에 해당하는 수를 모두 지운다.
arr[1] = 0
for i in range(2, n + 1):
    if arr[i] == 0:
        continue
    j = 2
    while i * j <= n:
        arr[i * j] = 0
        j += 1

prime_num = []
for i in range(n + 1):
    if arr[i] != 0:
        prime_num.append(i)
prime_num.insert(0, 0)
# print(prime_num)

## 투포인터 방법 사용해서 개수 count
start, end, cnt, sum = 0, 0, 0, 0
m = len(prime_num)
while end < m:
    if sum == n:
        cnt += 1
        end += 1
        if end < m:
            sum += prime_num[end]
    elif sum > n:
        sum -= prime_num[start]
        start += 1
    else:
        end += 1
        if end < m:
            sum += prime_num[end]

print(cnt)
