# 브루트 포스 - 17088번 - 등차수열 변환
## 등차수열의 개념 = **첫항** & **공차** 만 있으면 구할 수 있다.
## 첫항&공차 - 총 9가지 경우만 고려하면 됨
n = int(input())
b = list(map(int, input().split()))
op = [-1, 0, 1]
ans = float('INF')
if len(b) == 1:
    print(0)
    exit()

def op_num(a0, d):
    global ans
    result = 0
    for i in range(n):
        dif = b[i] - (a0 + d * i)
        if dif not in op:
            return
        result += abs(dif)
    # print('a0=%d, d=%d 일 때의 result=%d'%(a0, d, result))
    ans = min(ans, result)


for i in range(3):
    for j in range(3):
        a0 = b[0] + op[i]
        d = b[1] + op[j] - a0
        op_num(a0, d)

if ans == float('INF'):
    print(-1)
else:
    print(ans)
