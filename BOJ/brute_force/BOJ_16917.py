# 브루트 포스 - 16917번 - 양념 반 후라이드 반
## 양념가격 , 후라이드가격 , 반반가격 , 양념최소개수 , 후라이드최소개수
# 구해야 하는 값 : 주어진 개수만큼의 치킨을 사기 위한 최소 비용 -> 이 때 변하는 값 : 반반치킨의 구매 개수
## Q. 브루트포스라고 판단하는 기준이 있나? input 개수가 적을 때?? ㅇㅇ (+ 시간복잡도 고려)


import sys
input = sys.stdin.readline

v1, v2, v1_5, num1, num2 = map(int, input().split())
ans = v1 * num1 + v2 * num2
if v1_5 > v1 and v1_5 > v2:                 # 만약 반반치킨이 가장 비싼 경우 -> 양념&후라이드로만 조합한 결과 출력
    print(ans)
    exit()
for i in range(1, max(num1, num2)+ 1):  # i = 반반 치킨 주문 개수
    num1_5 = i * 2      # 구매한 양념치킨의 개수
    tmp = 2*i*v1_5 + max(0, num1-i) * v1 + max(0, num2-i)*v2        # 차례대로,, 반반치킨 가격 총합 + 양념치킨 가격 총합 + 후라이드치킨 가격 총합
    ans = min(ans, tmp)

print(ans)
