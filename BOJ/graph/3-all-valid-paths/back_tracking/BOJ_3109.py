# BFS (인데 백트래킹을 곁들인) - 3109번 - 빵집
import sys

sys.setrecursionlimit(10 ** 5)  # 최대 depth 만큼만 하면 되나?
input = sys.stdin.readline

dy = [-1, 0, 1]

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
# print(graph)

NO = 7

# (y, x) 에서 (y-1, x+1), (y, x+1), (y+1, x+1) 로 갈 수 있는지 확인하기
# def can_go(y, x, d, dir):
#     ny, nx = y + d, x + 1
#     print('(', y, ',', x, ') -> (', ny, ',', nx, ')', end=' ')
#     if graph[y][x] == '.' and graph[ny][nx] == '.':
#         if dir[y][x] == NO and dir[ny][nx] == NO:  # 해당 칸을 아직 아무도 사용하지 않음
#             # 크로스로도 엮이는 파이프가 없어야됨
#             if d == -1 and dir[y - 1][x] == 1:  # 지금 가려는 방향이 오른쪽 윗 대각선인 경우
#                 print('(X)')
#                 return False
#             if d == 1 and dir[y + 1][x] == -1:  # 지금 가려는 방향이 오른쪽 아래 대각선인 경우
#                 print('(X)')
#                 return False
#         print('(O)')
#         return True
#     print('(X)')
#     return False
def can_go(y, x, d, dir):
    ny, nx = y + d, x + 1
    if not (0 <= ny < R and 0 <= nx < C):
        return False
    if graph[y][x] == '.' and graph[ny][nx] == '.' and dir[ny][nx] == NO:
        if d == -1 and y - 1 >= 0 and dir[y - 1][x] == 1:
            return False
        if d == 1 and y + 1 < R and dir[y + 1][x] == -1:
            return False
        return True  # ✅ 조건 만족 시 True 반환
    return False

def dfs(dir, y, x):
    # print('ing = (', y, ',', x, ')')
    if x == C - 1:
        dir[y][x] = 1
        return True
    for d in dy:
        ny, nx = y + d, x+1
        # if 0 <= (y + d) < C and 0 <= nx < C and can_go(y, x, d, dir):
        if 0 <= ny < R and 0 <= nx < C and can_go(y, x, d, dir):
            dir[y][x] = d
            if dfs(dir, ny, nx):  # 이미 파이프 완성하고 온 경우
                return True
    dir[y][x] = -2      # 실패한 경로 마킹하기 : "어차피 이 길로 가면 파이프 실패하니까 중복 계산 제거해줌"
    return False

direction = [[NO] * C for _ in range(R)]
ans = 0
for i in range(R):
    # print('start')
    if dfs(direction, i, 0):
        ans += 1
        # for d in direction:
        #     print(d)
    # print()
print(ans)