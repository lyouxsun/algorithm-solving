# 그리디 알고리즘 - 10775번 - 공항
import sys
input = sys.stdin.readline
gate = int(input())
plane = int(input())
arr = [int(input()) for _ in range(plane)]
cnt = 0
parent = []
for i in range(gate):
    parent[i] = i
#####################################################
# 0~gate 딕셔너리 만들기
# 딕셔너리 탐색 (if [i]==i: value -1로 바꾸기 & i리턴 / else: value
# 부모 노드를 찾는 함수
def findParent(i):
    if parent[i] == i:
        parent[i] = -1
        return i
    parent[i] = findParent(parent, parent[i])
    return parent[i]


#####################################################
for _ in range(plane):
    tmp = int(input())
    findParent(tmp)
for i in range(tmp, -1, -1):
    if i == 0:
        break
    '''
    if result[i] == 0:
        result[i] = 1
        cnt += 1
        break
    
if i == 0:
    break
    '''
print(cnt)

