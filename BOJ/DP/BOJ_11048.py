# 동적 프로그래밍 - 11048번 - 이동하기
## arr와 크기가 똑같은 dp테이블 생성 후에 모든 지점에서 해당 지점까지의 사탕 수 최댓값을 저장
# -> dp[n][m] 을 출력 (bfs처럼 풀기)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(0, n):
    for j in range(0, m):
        if i == 0 and j == 0:
            continue
        if i == 0:
            arr[i][j] += arr[i][j - 1]
            continue
        if j == 0:
            arr[i][j] += arr[i - 1][j]
            continue
        arr[i][j] += max(arr[i][j - 1], arr[i - 1][j], arr[i - 1][j - 1])

# print(arr)
print(arr[n - 1][m - 1])
