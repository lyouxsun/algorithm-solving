# BFS - 2234번 - 성곽
## 그래프로 따지면 부분 그래프의 개수, 각 그래프의 크기 구하기
import sys
from collections import deque
input = sys.stdin.readline


# 1. 수를 비트마스킹 해서 벽 있없 파악하기
def wall(n):
    dir = [False] * 4  # 순서대로 동.서.남.북
    if (n & 1) == 1:  # 가장 오른쪽 비트가 1 = 서쪽에 벽이 있음
        dir[1] = True
    if (n & (1 << 1)) == 1:  # 오른쪽에서 2번째 비트가 1 = 북쪽에 벽이 있음
        dir[3] = True
    if (n & (1 << 2)) == 1:  # 오른쪽에서 3번째 비트가 1 = 동쪽에 벽이 있음
        dir[0] = True
    if (n & (1 << 3)) == 1:  # 가장 왼쪽 비트가 1 = 남쪽에 벽이 있음
        dir[2] = True
    return dir


# 2. 각 칸을 요소 index로 나타낸 g 배열 만들기 & 각 그룹의 크기를 저장하는 size 배열도 같이 만들기
c, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
idx = 0
g = [[0] * c for _ in range(r)]
size = []
for i in range(r):
    for j in range(c):


# 3. 붙어있는 2개의 그룹들의 합 구하기 -> 그 중 최댓값 출력
