# 부르트 포스 - 17127번 - 벚꽃이 정보섬에 피어난 이유

N = int(input())
result = 0
arr = list(map(int, input().split()))

def cal(start, end):
    ans = 1
    for a in range(start, end+1):
        ans *= arr[a]
    return ans


for i in range(N-3):
    for j in range(i+1, N-2):
        for k in range(j+1, N-1):
            tmp = cal(0, i) + cal(i+1, j) + cal(j+1, k) + cal(k+1, N-1)
            result = max(tmp, result)
print(result)
