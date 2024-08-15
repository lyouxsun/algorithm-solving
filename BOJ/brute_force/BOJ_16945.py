# 브루트 포스 - 16945번 - 매직 스퀘어로 변경하기
## 가능한 모든 3*3 매직스퀘어를 만든 후, 주어진 배열과의 차가 최소인 배열을 구한다
from itertools import permutations
sq = [list(map(int, input().split())) for _ in range(3)]
ans = 100

arrs = list(permutations(range(1, 10), 9))
def cost(arr):
    result = 0
    for i in range(3):
        for j in range(3):
            result += abs(sq[i][j] - arr[i][j])
    return result

for tmp in arrs:
    arr = [0]*3
    for i in range(3):
        arr[i] = tmp[3*i:3*(i+1)]
    # print(arr)
    # print('-'*20)
    if (arr[0][0] + arr[0][1] + arr[0][2] ==
            arr[1][0] + arr[1][1] + arr[1][2] ==
            arr[2][0] + arr[2][1] + arr[2][2] ==
            arr[0][0] + arr[1][0] + arr[2][0] ==
            arr[0][1] + arr[1][1] + arr[2][1] ==
            arr[0][2] + arr[1][2] + arr[2][2] ==
            arr[0][0] + arr[1][1] + arr[2][2] ==
            arr[0][2] + arr[1][1] + arr[2][0]):
        ans = min(ans, cost(arr))

print(ans)