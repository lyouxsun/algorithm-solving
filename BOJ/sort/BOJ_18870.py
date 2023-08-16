# 정렬 알고리즘 - 18870 - 좌표 압축
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
tmp = sorted(set(arr))
dic = {tmp[i]:i for i in range(len(tmp))}
for i in arr:
    print(dic[i], end=" ")