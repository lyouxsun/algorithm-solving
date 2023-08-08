# 그리디 알고리즘 - 1461번 - 도서관
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
minus = [-i for i in arr if i<0]
plus = [i for i in arr if i>0]
plus.sort()
minus.sort()

def calculate(arr, answer):
    if len(arr) % M != 0:
        answer += 2 * arr[len(arr) % M - 1]
        del arr[0:len(arr) % M]
    while len(arr) > 0:
        answer += 2 * arr[-1]
        for _ in range(M):
            arr.pop()
    return answer

if len(plus)==0:
    tmp = max(minus)
if len(minus)==0:
    tmp = max(plus)
if len(plus)!=0 and len(minus)!=0:
    if plus[-1] > minus[-1]:
        tmp = max(plus)
    else:
        tmp = max(minus)
answer = calculate(minus, calculate(plus, 0))-tmp
print(answer)