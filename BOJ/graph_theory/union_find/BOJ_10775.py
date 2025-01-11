# 그리디, union_find 알고리즘 - 10775번 - 공항
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
gate = int(input())
plane = int(input())
gates = [i for i in range(gate+1)]    # 처음 게이트는 자기 자신만 가리키도록 설정
arr = [int(input()) for _ in range(plane)]      # 비행기 들어오는 순서대로 배열에 넣기
cnt = 0
def find(i):
    if gates[i] == i:
        gates[i] = i-1
        return i
    gates[i] = find(gates[i])
    return gates[i]

for i in arr:
    if find(i) == 0:
        break
    cnt += 1
print(cnt)