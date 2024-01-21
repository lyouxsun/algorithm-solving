# 이 두줄을 추가하니까 수행시간이 좀 줄었다
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B의 첫번째 원소가 A에 존재하면 그 인덱스부터 차례대로 일치 여부 확인
# 조건문과 반복문이 너무 난잡하게 구성되어 있음..
# while True:
#     idx = -1
#     if B[0] in A:
#         idx = A.index(B[0])
#         if idx+b > a:
#             print('No')
#             break
#         for i in range(b):
#             if A[idx+i] != B[i]:
#                 A = A[idx+i:]
#                 break
#             if i == b-1:
#                 print('Yes')
#                 idx = -2
#                 break
#         if idx == -2:
#             break
#     else:
#         print('No')
#         break

# 하나의 배열이 다른 배열에 속하는지는 알 수 없으나, 둘이 일치하는지 여부는 알 수 있다는 점 활용
# A를 B 크기 만큼 조각 내어 각각이 B와 일치하는지 확인
# 수행 시간은 비슷하나 코드가 더 짧고 효율적이다.
success = False
for i in range(a-b+1):
    tmp = A[i:i+b]
    if tmp == B:
        success = True
        break

if success:
    print('Yes')
else:
    print('No')