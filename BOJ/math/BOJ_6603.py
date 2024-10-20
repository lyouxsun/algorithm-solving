# 수학 - 6603번 - 로또

from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    num = arr.pop(0)
    comb = combinations(arr, 6)
    for c in comb:
        for num in c:
            print(num, end=' ')
        print()
    print()