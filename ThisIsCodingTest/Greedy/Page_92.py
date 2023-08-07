# 92p - 큰 수의 법칙
## 아이디어 : 숫자가 커진다면 시간초과가 날 수도 있는 비효율적인 방법
'''
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
total = 0
cnt = 0
for i in range(M):
    if cnt<K:
        total += arr[0]
        cnt+=1
    else:
        total += arr[1]
        cnt=0
print(total)
'''

## 아이디어 : 반복되는 수열이라는 아이디어에서 착안
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
max1 = arr[0]
max2 = arr[1]

# max1, max2가 더해지는 횟수 구하기
cnt2 = M//(K+1)
cnt1 = M - cnt2
total = cnt1*max1 + cnt2*max2
print(total)