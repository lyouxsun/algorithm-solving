# 그리디 알고리즘 - 1026번 - 보물
## sum += B의 n번째로 큰 수 * A의 n번째로 작은 수
import sys
N = sys.stdin.readline()
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
sum=0

while len(a)>0:
    sum += min(a)*max(b)
    del a[a.index(min(a))]
    del b[b.index(max(b))]
print(sum)