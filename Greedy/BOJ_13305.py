# 그리디 알고리즘 - 13305번 - 주유
## 1.도시개수 2.거리 3.기름값
## 기름값이 제일 싼 곳을 구하고 (=min) 그 뒤는 (남은 거리)*min
import sys
N = int(sys.stdin.readline())
distance = [*map(int,sys.stdin.readline().split(' '))]
price = [*map(int,sys.stdin.readline().split(' '))]
total=0
tmpDis=0
minimum=price[0]

for i in range(N-1):
    if minimum>=price[i]:
        minimum=price[i]
    total += minimum * distance[i]
# 다음기름값이 더 비쌈 -> 다다음 값도 비교 -> 자기와 작은게 나오기 전까지의 거리의 합을 구함
print(total)