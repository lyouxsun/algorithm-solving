# 브루트 포스 - 16638번 - 괄호 추가하기 2
## DFS(재귀) 백트래킹으로ㄱㄱ

n = int(input())
exp = list(input())
for i in range(0, n, 2):
    exp[i] = int(exp[i])
ans = -1 * 2 ** 31


def cal(e):
    arr = []
    i = 0
    m = len(e)
    # print('곱셈 계산 전 = ', e)

    while i < m:  # 곱셈 우선 계산
        if i+1 < m and e[i + 1] == '*':
            tmp = e[i]
            while i + 2 < m and e[i + 1] == '*':  # 연속된 곱셈 처리
                tmp *= e[i + 2]
                i += 2
            arr.append(tmp)
        else:
            arr.append(e[i])
        i += 1

    # print('곱셈 계산 후 = ',arr)
    result = arr[0]
    for j in range(1, len(arr)-1, 2):  # 나머지 계산
        if arr[j] == '+':
            result += arr[j + 1]
        elif arr[j] == '-':
            result -= arr[j + 1]

    global ans
    ans = max(ans, result)
    return result


# expression : 지금까지 변경된 수식
# idx : 마지막 괄호 위치
# br : 남은 괄호 수
def dfs(expression, idx, br):
    e = expression[:]
    apply_bracket(e, idx)  # apply_bracket : 괄호 추가한 부분만 계산
    if br == 0:
        cal(e)             # cal : 식 전체 계산
        return
    if idx + 4 >= n:
        return
    for i in range(idx + 4, n, 2):
        dfs(e, i, br - 1)


def apply_bracket(e, idx):
    if e[idx] == '*':
        e[idx - 1] *= e[idx + 1]
    elif e[idx] == '+':
        e[idx - 1] += e[idx + 1]
    else:
        e[idx - 1] -= e[idx + 1]
    e[idx] = '*'
    e[idx + 1] = 1


if len(exp) == 1:
    print(exp[0])
    exit(0)
if n == 3:
    print(cal(exp))
    exit(0)

br_num = (n // 2 + 1) // 2
for i in range(br_num+1):  # 괄호의 개수
    if i == 0:
        ans = max(ans, cal(exp))
        continue
    for j in range(1, n, 2):
        dfs(exp, j, i-1)
print(ans)
