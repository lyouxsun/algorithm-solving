import copy

# 얕은 복사할 때 값 변경
arr1 = [1, 2, 3, 4, [5, 6, 7]]
arr2 = arr1[:]
print('arr1 : ', arr1)
print('arr2 : ', arr2)

# 1. [:] 얕은 복사 후 arr2의 값을 변경해도 arr1은 바뀌지 않는다!!
print('[:] 얕은 복사 후 immutable 값 변경')
arr2[3] = 11
print('arr2[3] = 11')
print('arr1 : ', arr1)
print('arr2 : ', arr2)

# 2. [:] 얕은 복사 후 arr2 리스트 내부의 리스트를 변경하면 arr1도 바뀐다!!
print()
print('[:] 얕은 복사 후 리스트 내부 리스트 (mutable 값) 변경')
arr2[4][2] = 12
print('arr2[4][2] = 12')
print('arr1 : ', arr1)
print('arr2 : ', arr2)


# 3. BOJ 14502번 - 연구소 예제
print()
print('BOJ 14502번 연구소 예제 shallow copy 테스트')
arr = [[2, 0, 0, 0, 1, 1, 0],
       [0, 0, 1, 0, 1, 2, 0],
       [0, 1, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1],
       [0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0]]
shallow_copy_arr = arr[:]
# deep_copy_arr = copy.deepcopy(arr)
for i in range(7):
    for j in range(7):
        if arr[i][j] == 0:
            shallow_copy_arr[i][j] = 2
print('arr : ', arr)
print('shallow_copy_arr : ', shallow_copy_arr)
# print('deep_copy_arr : ', deep_copy_arr)

