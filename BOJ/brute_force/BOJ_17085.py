# 브루트 포스 - 17085번 - 십자가 2개 놓기
import sys, copy

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0] * n
for i in range(n):
    arr[i] = list(input().strip())
r1, r2 = 0, 0
ans = 0


def search(copy_arr, r, c):
    copy_arr[r][c] = '*'
    k = 1
    while True:
        if not (k <= r < n - k) or not (k <= c < m - k):
            break
        if (copy_arr[r][c - k] == '#') and (copy_arr[r][c + k] == '#') and (
                copy_arr[r - k][c] == '#') and (copy_arr[r + k][c] == '#'):
            copy_arr[r][c - k] = '*'
            copy_arr[r][c + k] = '*'
            copy_arr[r - k][c] = '*'
            copy_arr[r + k][c] = '*'
            k += 1
        else:
            break
    size = 1 + 4 * (k - 1)
    return size


for i1 in range(n):
    for j1 in range(m):
        if arr[i1][j1] == '#':
            copy_arr = copy.deepcopy(arr)
            for s1 in range(n):
                if not (s1 <= i1 < n - s1) or not (s1 <= j1 < m - s1):
                    break
                if (copy_arr[i1][j1 - s1] == '#') and (copy_arr[i1][j1 + s1] == '#') and (
                        copy_arr[i1 - s1][j1] == '#') and (copy_arr[i1 + s1][j1] == '#'):
                    copy_arr[i1][j1 - s1] = '*'
                    copy_arr[i1][j1 + s1] = '*'
                    copy_arr[i1 - s1][j1] = '*'
                    copy_arr[i1 + s1][j1] = '*'
                else:
                    break
                for i2 in range(n):
                    for j2 in range(m):
                        if copy_arr[i2][j2] == '#':
                            for s2 in range(n):
                                if not (s2 <= i2 < n - s2) or not (s2 <= j2 < m - s2):
                                    break
                                if (copy_arr[i2][j2 - s2] == '#') and (copy_arr[i2][j2 + s2] == '#') and (
                                        copy_arr[i2 - s2][j2] == '#') and (copy_arr[i2 + s2][j2] == '#'):
                                    ans = max(ans, (1 + s1 * 4) * (1 + s2 * 4))
                                else:
                                    break
                            # if ans < r1*r2:
                            #     print('[ans = %d] i1 = %d, j1 = %d, i2 = %d, , j2 = %d'%(r1*r2, i1, j1, i2, j2))


print(ans)

# 5 8
# ..#..#..
# ..#..#..
# ########
# ..#..#..
# ..#..#..
# 정답=25  -> 이 경우 때문에 최대 크기만 고려하면 오답. 모든 경우에 대해 2번째 십자가의 크기를 구해야한다.