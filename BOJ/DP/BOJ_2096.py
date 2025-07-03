# dp - 2096번 - 내려가기
# 메모리 이슈 -> 배열 왕창 선언하는게 아니라 작게 선언해서 재활용하기!!
import sys
input = sys.stdin.readline

n = int(input())
max_tree = [[0] * 3 for _ in range(2)]
min_tree = [[0] * 3 for _ in range(2)]
line = list(map(int, input().split()))
for i in range(3):
    max_tree[0][i] = line[i]
    min_tree[0][i] = line[i]
p = 0

for i in range(1, n):
    line = list(map(int, input().split()))
    p = 1 - p
    min_tree[p][0] = line[0] + min(min_tree[1 - p][0], min_tree[1 - p][1])
    min_tree[p][1] = line[1] + min(min_tree[1 - p][0], min_tree[1 - p][1], min_tree[1 - p][2])
    min_tree[p][2] = line[2] + min(min_tree[1 - p][1], min_tree[1 - p][2])

    max_tree[p][0] = line[0] + max(max_tree[1 - p][0], max_tree[1 - p][1])
    max_tree[p][1] = line[1] + max(max_tree[1 - p][0], max_tree[1 - p][1], max_tree[1 - p][2])
    max_tree[p][2] = line[2] + max(max_tree[1 - p][1], max_tree[1 - p][2])

print(max(max_tree[p]), min(min_tree[p]))
