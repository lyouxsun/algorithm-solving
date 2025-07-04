# 유니온 파인드 - 1717번 - 집합의 표현
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]


def get_parent(parent, v):
    # print(v, '의 root = ', parent[v])
    if parent[v] == v:
        return v
    # 경로 압축
    # parent[v] = get_parent(parent, v)     # 이렇게 해서 무한루프 발생ㅠ
    parent[v] = get_parent(parent, parent[v])
    return parent[v]


# 두 노드를 하나의 집합으로 합칠 때
def union(parent, v1, v2):
    v1_parent = get_parent(parent, v1)
    v2_parent = get_parent(parent, v2)

    # if v1_parent < v2_parent:     # 이렇게 해도 무한루프 발생ㅠ
    #     parent[v2] = v1_parent
    # else:
    #     parent[v1] = v2_parent
    if v1_parent < v2_parent:
        parent[v2_parent] = v1_parent
    else:
        parent[v1_parent] = v2_parent


# 둘이 합집합인지 확인 후 T/F 반환
def find(parent, v1, v2):
    v1_parent = get_parent(parent, v1)
    v2_parent = get_parent(parent, v2)
    if v1_parent == v2_parent:
        return True
    return False


for i in range(M):
    Q, a, b = map(int, input().split())
    if Q == 0:
        union(parent, a, b)
    else:
        if a == b or find(parent, a, b):
            print("YES")
        else:
            print("NO")