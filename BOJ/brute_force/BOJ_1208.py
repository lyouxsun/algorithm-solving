# 중간에서 만나기 - 1208번 - 부분수열의 합2
## 1, 크기가 너무 크니까 절반으로 나누자!!
## 2. 절반으로 나눈 수열에서 나올 수 있는 모든 부분수열의 합 구하기
## 3. 두 수열의 합 중 각각 하나씩을 골라서, 합이 S가 되는 경우를 세면 된다!
from itertools import combinations

m, s = map(int, input().split())
arr = list(map(int, input().split()))

if m == 1:
    if arr[0] == s:
        print(1)
    else:
        print(0)
    exit()

a1 = arr[:m // 2]
a2 = arr[m // 2:]


def sub_sum(array):
    sums = []
    n = len(array)
    for i in range(n + 1):
        for comb in combinations(array, i):
            sums.append(sum(comb))
    return sums


s1 = sub_sum(a1)
s2 = sub_sum(a2)

s1.sort()
s2.sort(reverse=True)

# 투포인터 방식으로 모든 경우의수 구하기
p1, p2, cnt = 0, 0, 0  # 포인터
while p1 < len(s1) and p2 < len(s2):
    current_sum = s1[p1] + s2[p2]
    if current_sum == s:
        c1 = 1  # s1에서 s1[p1]의 개수
        c2 = 1  # s2에서 s2[p2]의 개수
        p1 += 1
        p2 += 1
        while p1 < len(s1) and s1[p1] == s1[p1 - 1]:
            c1 += 1
            p1 += 1
        while p2 < len(s2) and s2[p2] == s2[p2 - 1]:
            c2 += 1
            p2 += 1
        cnt += c1 * c2
    elif current_sum < s:
        p1 += 1
    else:
        p2 += 1

if s == 0:
    cnt -= 1  # 아무것도 선택 안한 경우 제외하기
print(cnt)
