# 브루트 포스 - 16637번 - 괄호 추가하기
import math

n = int(input())
exp = list(input())
num = math.ceil(n / 2)  # 식에서 숫자의 개수
ans = -float('INF')
for i in range(num):
    exp[2 * i] = int(exp[2 * i])


def dfs(current_exp, idx, num):  # idx : 마지막 괄호 위치, num : 남은 괄호 개수
    if idx >= n - 1 or num == 0:
        return

    # 괄호 있을 때 연산 진행
    new_exp = current_exp[:]
    if new_exp[idx + 1] == '+':
        new_exp[idx] += new_exp[idx + 2]
    elif new_exp[idx + 1] == '-':
        new_exp[idx] -= new_exp[idx + 2]
    elif new_exp[idx + 1] == '*':
        new_exp[idx] *= new_exp[idx + 2]
    new_exp[idx + 1] = '+'
    new_exp[idx + 2] = 0

    # 끝나는 기준
    if num == 1:
        global ans
        ans = max(ans, calculate(new_exp))
        return

    # 재귀 호출
    for j in range(idx + 4, n-1, 2):
        dfs(new_exp, j, num - 1)


def calculate(arr):
    result = arr[0]
    for i in range(1, len(arr), 2):
        if arr[i] == '+':
            result += arr[i + 1]
        elif arr[i] == '-':
            result -= arr[i + 1]
        elif arr[i] == '*':
            result *= arr[i + 1]
    return result


for i in range(num // 2 + 1):  # 괄호의 개수
    if i == 0:
        ans = max(ans, calculate(exp))
        continue
    for j in range(num):  # 괄호 시작 위치
        br = 2 * j
        if br + 2 < n:
            arr = exp[:]
            dfs(arr, br, i)
print(ans)
