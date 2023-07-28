# 그리디 알고리즘 - 2437번 - 저울
## 주어진 추로 측정할 수 있는 무게의 범위 구하기 -> 추가 추가될 때마다 범위가 늘어나는데,
## 그때 새로운 범위는 연속되는가,, 연속이 안되면 그 중에서 최솟값==답
# 1 1 2 3 6 7 30
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
target = 1
for i in arr:
    if target < i:
        break
    target += i
print(target)