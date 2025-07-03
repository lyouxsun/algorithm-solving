# 유니온 파인드 - 17471번 - 게리멘더링
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# 1. 입력 받고 그래프로 초기화
N = int(input())
NODES = list(map(int, input().split()))
edges = set()

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    if line[0] == 0:
        continue
    line.pop(0)
    for n in line:
        edges.add((i, n))
        edges.add((n, i))
edges = list(edges)


# 2. 전체 유니온 파인드
# -> 구역이 3개 이상이면 -1 출력 후 종료
# -> 구역이 2개면 추가 계산 없이 각 구현의 차만 계산해서 출력
# (이제 하나의 구역으로 이어진 경우만 남음)
def find(parent, n):
    if parent[n] != n:
        parent[n] = find(parent, parent[n])  # 경로 압축
    return parent[n]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a

# 집합 개수 세기
def count_groups(parent, N):
    roots = set()
    for i in range(1, N + 1):
        roots.add(find(parent, i))
    return len(roots)

# 각 그룹에 포함된 노드 파악
def get_groups(parent, N):
    groups = dict()
    for i in range(1, N + 1):
        root = find(parent, i)      # 대표자 찾기
        if root not in groups:
            groups[root] = []       # 리스트 초기화
        groups[root].append(i)
    return groups

parent = [0] * (N+1)
group_cnt = count_groups(parent, N)
if group_cnt > 2:
    print(-1)
    sys.exit()
if group_cnt == 2:
    groups = get_groups(parent, N)
    group_keys = list(groups.keys())
    first_group_sum, second_group_sum = 0, 0
    for nodes in group_keys[0]:
        first_group_sum += NODES[nodes]
    for nodes in group_keys[1]:
        second_group_sum += NODES[nodes]
    print(abs(first_group_sum - second_group_sum))
    sys.exit()

# 3. 각 노드가 1번째 구역 O/X인 경우 모두 계산 (brute force)
# 3-1. 이 그래프에서 1번째 구역, 2번째 구역 각각이 연결되어 있는지 확인
# -> 연결 안 되어 있으면 다음 경우의 수로ㄱ
# -> 연결 되어 있으면 각 구역의 합 계산 후 min 비교해서 ans 갱신
# 4. 다 계산한 후 최종 ans 출력
graph = {i: [] for i in range(1, N + 1)}            # 인접 리스트 생성: 노드 번호를 key로 하여 연결된 노드를 리스트로 저장
for a, b in edges:
    graph[a].append(b)

def is_connected(group, graph):         # 특정 그룹이 내부적으로 모두 연결되어 있는지 확인하는 함수 (BFS 기반)
    visited = set()
    q = deque()

    start = next(iter(group))  # 그룹 내 아무 노드 하나로 시작
    q.append(start)
    visited.add(start)

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor in group and neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    return visited == group  # 모든 노드를 방문했는지로 연결 여부 판단

INF = float('inf')          # 가능한 모든 두 그룹 분할 조합을 생성하여 탐색 (brute force) : 그룹 A와 B가 모두 연결되어 있는 경우만 인구 차이 계산
min_diff = INF
all_nodes = set(range(1, N + 1))

for r in range(1, N // 2 + 1):  # 절반까지만 (대칭 제거)
    for a_group in combinations(all_nodes, r):
        a_set = set(a_group)
        b_set = all_nodes - a_set

        if is_connected(a_set, graph) and is_connected(b_set, graph):
            a_sum = sum(NODES[i - 1] for i in a_set)  # NODES는 0-indexed
            b_sum = sum(NODES[i - 1] for i in b_set)
            diff = abs(a_sum - b_sum)
            min_diff = min(min_diff, diff)

print(min_diff if min_diff != INF else -1)      # 최종 정답 출력 : # 모든 경우를 시도한 후 최소 인구 차이를 출력 (불가능하면 -1)