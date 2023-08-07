# 96p - 숫자 카드 게임
## 아이디어 : 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰수를 찾기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
minArr = []
for i in range(N):
    tmp = list(map(int, input().split()))
    minArr.append(min(tmp))
print(max(minArr))