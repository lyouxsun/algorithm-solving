# 그리디 알고리즘 - 1041번 - 주사위
import sys
input = sys.stdin.readline
N = int(input())
tmp = list(map(int, input().split()))
if N == 1:
    total = sum(tmp)-max(tmp)
else:
    #  min(arr)가 여러개인지 확인 -> 여러개면 arr[5-arr.index(min(arr))] 중 가장큰 값 del
    arr=[]
    arr.append(min(tmp[0], tmp[5]))
    arr.append(min(tmp[1], tmp[4]))
    arr.append(min(tmp[2], tmp[3]))
    arr.sort()
    total = arr[2]*4 + arr[1]*(2*N-2)*4 + arr[0]*(5*N*N-8*N+4)
print(total)