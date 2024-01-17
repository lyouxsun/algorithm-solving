n = int(input())
arr = list(map(int, input().split()))
ans = []

for i in arr:
    if i % 2 == 0:
        ans.append(i)
for i in ans[::-1]:
    print(i, end=' ')