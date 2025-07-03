# DP - 11057번 -  오르막 수
## 점화식 : 일의 자리 수로 k가 왔을 때의 개수 규칙이 존재!!

n = int(input())
arr = [[1]* 10 for _ in range(n+1)]

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i][j-1] + arr[i-1][j]
ans = 0
for i in range(10):
    ans += arr[n][i]
print(ans%10007)