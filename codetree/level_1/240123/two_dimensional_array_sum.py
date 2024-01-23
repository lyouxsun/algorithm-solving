arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    print(f'{sum(arr[i])/4:.1f}', end=' ')
print()

for i in range(4):
    print(f'{(arr[0][i]+arr[1][i])/2:.1f}', end = ' ')
print()

print(f'{(sum(arr[0])+sum(arr[1]))/8:.1f}')