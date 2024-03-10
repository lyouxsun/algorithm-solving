# 11403번 - 그래프 탐색 - 경로 찾기
## 플로이드 워셜 알고리즘을 사용하여 모든 노드에서 모든 노드로 가는 최단경로를 탐색
# (DP -> 테이블 사용)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):  # i : 거쳐가는 노드
    for j in range(n):  # j -> k 로 가는 경우
        for k in range(n):
            if arr[j][k] == 0:
                if (arr[j][i] == 1) and (arr[i][k] == 1):
                    arr[j][k] = 1
# print(arr)
for y in range(n):
    for x in range(n):
        print(arr[y][x], end=' ')
    print()
