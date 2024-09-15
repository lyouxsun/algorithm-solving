# 세그먼트 트리 - 2243번 - 사탕상자
## 사탕을 넣을 때마다 리프노드를 항상 초기화 & 정렬
## 리프노드에는 (사탕의 맛, 개수) 튜플로 저장. 부모노드에는 사탕의 개수 합만 저장
import sys

input = sys.stdin.readline

num = int(input())  # 주어질 연산의 개수
func = []
for i in range(num):
    func.append(list(map(int, input().split())))
candy = []

n = 0  # 세그먼트 트리에 들어갈 숫자의 개수
for f in func:
    if f[0] == 2:
        n += 1
# print(n)
k = 0
while n > 2 ** k:
    k += 1
candy = [0] * 1000001
seg = [0] * (1 << 21)       # 1000000개가 들어갈 수 있는 세그먼트트리 크기


## 이분탐색 적용해서 시간 줄이기!!
def update_seg(cur, start, end, idx, new):  # cur=현재위치 / start~end=변경할범위 / idx=변경된사탕의위치 / num=변경된사탕의개수
    # print('재정렬 전 seg =', seg)
    if idx < start or idx > end:
        return
    seg[cur] += new
    if start != end:
        mid = (start + end) // 2
        update_seg(cur * 2, start, mid, idx, new)
        update_seg(cur * 2 + 1, mid + 1, end, idx, new)


def find_seg(cur, start, end, find):  # cur=현재위치 / start~end=탐색범위 / find=찾는사탕의순위
    # 리프노드까지 가서 -> 그 노드의 seg[i][0]을 출력한 후, seg[i][1] -= 1 까지 하면 끝!!
    if start == end:
        return start
    mid = (start + end) // 2
    if seg[cur * 2] >= find:
        return find_seg(cur * 2, start, mid, find)
    else:
        return find_seg(cur * 2 + 1, mid + 1, end, find - seg[cur * 2])

for f in func:
    if f[0] == 2:
        update_seg(1, 1, 1000000, f[1], f[2])
    if f[0] == 1:
        candy = find_seg(1, 1, 1000000, f[1])
        print(candy)
        update_seg(1, 1, 1000000, candy, -1)
