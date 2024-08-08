# 브루트 포스 - 15686번 - 치킨 배달
## 집의 개수가 적으니까 치킨집 개수를 줄이는 모든 경우의 고려할 수 있을듯
## bfs로 치킨집과의 최단 거리 구함
## 경우의 수 = 치킨집_C_m
import itertools

n, m = map(int, input().split())
arr = []
chicken = []
house = []

for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(n):
        if line[j] == 1:
            house.append([i, j])
        if line[j] == 2:
            chicken.append([i, j])

# 치킨집을 없앤 배열 만들고, 그걸 반복하는 로직
tmp = list(itertools.combinations(chicken, m))
combinations = [list(combo) for combo in tmp]
# print('combination = ', combinations)
ans = float('INF')
for case in combinations:
    distance = 0
    for h in house:
        tmp = float('INF')
        for c in case:
            tmp = min(tmp, abs(h[0]-c[0])+abs(h[1]-c[1]))
        distance += tmp
    ans = min(ans, distance)

print(ans)
