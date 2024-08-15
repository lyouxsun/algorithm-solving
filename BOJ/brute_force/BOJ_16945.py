# 브루트 포스 - 16945번 - 매직 스퀘어로 변경하기
## 가능한 모든 3*3 매직스퀘어를 만든 후, 주어진 배열과의 차가 최소인 배열을 구한다
from itertools import permutations
sq = [list(map(int, input().split())) for _ in range(3)]
ans = 100

def cost(arr):
    result = 0
    for i in range(3):
        for j in range(3):
            result += abs(sq[i][j] - arr[i][j])
    return result

## sol 1) 모든 3*3 배열 고려하기
# arrs = list(permutations(range(1, 10), 9))
# for tmp in arrs:
#     arr = [0]*3
#     for i in range(3):
#         arr[i] = tmp[3*i:3*(i+1)]
#     if (arr[0][0] + arr[0][1] + arr[0][2] ==
#             arr[1][0] + arr[1][1] + arr[1][2] ==
#             arr[2][0] + arr[2][1] + arr[2][2] ==
#             arr[0][0] + arr[1][0] + arr[2][0] ==
#             arr[0][1] + arr[1][1] + arr[2][1] ==
#             arr[0][2] + arr[1][2] + arr[2][2] ==
#             arr[0][0] + arr[1][1] + arr[2][2] ==
#             arr[0][2] + arr[1][1] + arr[2][0]):
#         # print(tmp)
#         # print()
#         ans = min(ans, cost(arr))

## sol 2) sol1을 통해 구한 매직 스퀘어 8개만 비교하기
arrs = [(2, 7, 6, 9, 5, 1, 4, 3, 8),
        (2, 9, 4, 7, 5, 3, 6, 1, 8),
        (4, 3, 8, 9, 5, 1, 2, 7, 6),
        (4, 9, 2, 3, 5, 7, 8, 1, 6),
        (6, 1, 8, 7, 5, 3, 2, 9, 4),
        (6, 7, 2, 1, 5, 9, 8, 3, 4),
        (8, 1, 6, 3, 5, 7, 4, 9, 2),
        (8, 3, 4, 1, 5, 9, 6, 7, 2)]
for tmp in arrs:
    arr = [0]*3
    for i in range(3):
        arr[i] = tmp[3*i:3*(i+1)]
    ans = min(ans, cost(arr))

print(ans)