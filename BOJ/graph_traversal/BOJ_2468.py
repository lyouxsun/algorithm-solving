# 그래프 탐색 - 2468번 - 안전 영역

import sys
sys.setrecursionlimit(10 ** 6)

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]


def dfs(h, w, visited):
    visited[h][w] = 1
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if (0 <= nh < n) and (0 <= nw < n):
            if visited[nh][nw] == 0:
                if arr[nh][nw] > rain:
                    dfs(nh, nw, visited)


def find(rain):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for h in range(n):
        for w in range(n):
            if visited[h][w] == 0 and arr[h][w] > rain:
                dfs(h, w, visited)
                cnt += 1
    return cnt


# 1. 그래프 입력 받기
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 2. 최솟값 최댓값 구하기
min_value = min(map(min, arr))
max_value = max(map(max, arr))

# 3. 최솟값 <= 강수량 < 최댓값 인 모든 경우를 고려하려 그래프의 요소 개수 구하기
cnt = [1]
for rain in range(min_value, max_value):
    cnt.append(find(rain))
print(max(cnt))

# 어떻게 하고 싶냐면, 강수량마다 그래프를 새롭게 탐색해야 하잖아
# rain -> find : 방문배열 만들어 주기, 배열의 모든 부분 탐색(dfs 호출, 방문 처리)하며 요소 개수 카운트 -> 요소 개수 리턴


# 예외처리 : 그래프의 모든 요소가 같은 수이면 min_value == max_value 여서 3번 과정에 있는 for문이 돌지 않는다
#          그럼 max(비어있는 배열) 을 계산할 때 런타임 에러 (ValueError)가 발생
# -> 비가 아예 오지 않을 때를 고려하면 요소개수는 항상 1 이상이니까 이 값을 cnt배열을 초기화할 때 넣어놓자!
