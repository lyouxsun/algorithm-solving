# A
import sys
input = sys.stdin.readline
arr = set()
for i in range(2, 10):
    arr.add(i)
    for j in range(1, 10):
        if i * j > 100:
            break
        arr.add(j)
        arr.add(i*j)
# print(arr)
n = int(input())
if n in arr:
    print(1)
else:
    print(0)