n = int(input())
arr = list(map(int, input().split()))
s1 = set()

# 중복되는 수는 set에 저장
for i in range(n):
    if arr.count(arr[i]) != 1:
        s1.add(arr[i])

# set에 있는 수는 arr에서 모두 제거
for i in s1:
    while arr.count(i) != 0:
        del arr[arr.index(i)]

# arr의 max 출력 (arr가 비어있으면 -1 출력)
if len(arr) == 0:
    print('-1')
else:
    print(max(arr))