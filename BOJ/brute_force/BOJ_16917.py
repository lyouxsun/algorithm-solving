# 브루트 포스 - 16917번 - 양념 반 후라이드 반
## 양념가격 , 후라이드가격 , 반반가격 , 양념최소개수 , 후라이드최소개수
## Q. 브루트포스라고 판단하는 기준이 있나? input 개수가 적을 때??


import sys
input = sys.stdin.readline

v1, v2, v1_5, num1, num2 = map(int, input().split())
ans = v1 * num1 + v2 * num2
if v1_5 > v1 and v1_5 > v2:                 # 만약 반반치킨이 가장 비싼 경우 -> 양념&후라이드로만 조합한 결과 출력
    print(ans)
    exit()
for i in range(1, max(num1, num2) * 2 + 1):  # i = 반반 치킨 주문 개수
    num1_5 = i
    tmp = v1_5 * num1_5
    if (num1 - num1_5 // 2) > 0:            # ex) 반반치킨 1마리 시켰으면 양념/후라이드 치킨은 num-(1//2) = num - 0 마리 더 시켜야됨
        tmp += v1 * (num1 - num1_5 // 2)
    if (num2 - num1_5 // 2) > 0:
        tmp += v2 * (num2 - num1_5 // 2)

    # print("양념개수=", (num1 - num1_5 // 2), "후라이드개수=", (num2 - num1_5 // 2), "반반개수=", num1_5)
    ans = min(ans, tmp)

print(ans)
