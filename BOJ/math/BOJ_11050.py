a, b = map(int, input().split())
answer = 1
tmp = a
for _ in range(b):
    answer *= tmp
    tmp -= 1
for i in range(1, b+1):
    answer /= i
print("%d" %answer)