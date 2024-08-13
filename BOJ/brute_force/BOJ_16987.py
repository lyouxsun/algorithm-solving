# 브루트 포스 - 16987번 - 계란으로 계란치기
import copy

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))
ans = 0


def dfs(eggs, attack):
    global ans

    # 종료 조건
    if attack >= n:
        broken_cnt = sum(1 for egg in eggs if egg[0] <= 0)
        ans = max(ans, broken_cnt)
        # print('111 =', eggs, ', ans =', ans)
        return

    # 잡고 있던 계란이 깨진 경우 or 바닥에 있는 모든 계란이 깨진 경우
    if eggs[attack][0] <= 0 or all(eggs[i][0] <= 0 for i in range(n) if i != attack):
        # print('222 =', eggs)
        dfs(eggs, attack + 1)
        return

    # 돌아가면서 (공격 -> 데미지 -> 원상복구)
    for defense in range(n):
        if (attack != defense) and (eggs[defense][0] > 0):
            tmp_attack = eggs[attack][0]
            tmp_defense = eggs[defense][0]

            eggs[attack][0] -= eggs[defense][1]
            eggs[defense][0] -= eggs[attack][1]

            dfs(eggs, attack + 1)

            # 원상복구
            eggs[attack][0] = tmp_attack
            eggs[defense][0] = tmp_defense



if n == 1:
    print(0)
    exit(0)
dfs(arr, 0)
print(ans)
