arr1 = [list(map(int, input().split())) for _ in range(3)]
input()     # 두 배열 사이의 엔터를 제거하기 위해 씀
arr2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        arr1[i][j] *= arr2[i][j]
        print(arr1[i][j], end = ' ')
    print()