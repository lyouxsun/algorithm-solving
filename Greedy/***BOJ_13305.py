# 그리디 알고리즘 - 13305번 - 주유
## 1.도시개수 2.거리 3.기름값
## 기름값이 제일 싼 곳을 구하고 (=min) 그 뒤는 (남은 거리)*min

N = int(input())
distance = [*map(int,input().split(' '))]
price = [*map(int,input().split(' '))]
total=0
tmpDis=0
min=0

for i in range(0,N-1):
    if(price[i]>=price[i+1]):
        tmpDis += distance[i]
        total += price[min] * tmpDis
        tmpDis = 0
        i+=1
    else:
        tmpDis += distance[i]
    if (tmpDis == 0):
        min = i

# 다음기름값이 더 비쌈 -> 다다음 값도 비교 -> 자기와 작은게 나오기 전까지의 거리의 합을 구함
print(total)