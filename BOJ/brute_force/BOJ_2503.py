# 브루트 포스 - 2503번 - 숫자 야구
## 모든 3자리 수를 만든 후에 조건에 만족하는 수만 남기자!
from itertools import permutations

# 1. 입력 받기
n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
# print(arr)

# 2. 모든 수 만들기
tmp = list(permutations(range(1, 10), 3))
# print(tmp)
can = []
for i in tmp:
    can.append(int(''.join(map(str, i))))
# print(can)

# 3. 모든 수에 대해서 모든 조건이 만족하는지 확인하기
def check(num, idx):
    test_num, s, b = arr[idx]
    num, test_num = str(num), str(test_num)
    total_strike = sum(na == nb for na, nb in zip(num, test_num))
    total_ball = len(set(num) & set(test_num)) - total_strike
    return (total_strike, total_ball) == (s, b)


ans = 0
for i in can:
    flag = True
    for j in range(n):
        if not check(i, j):
            flag = False
            break
    if flag:
        # print(i)
        ans += 1
print(ans)