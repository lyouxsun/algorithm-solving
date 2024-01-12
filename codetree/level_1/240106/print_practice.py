# f-string 사용하여 출력
name = '이영선'
score = 100
num = 1
print(f'이름 : {name}, 성적 : {score}, 등수 : {num}')
a = 3.141592
print("{0:.3f}".format(a))

# 입력받기 -> input()은 항상 문자열로 입력받음
m, n = input().split()
print(m, n)

# 별찍기 예제 1
a = int(input())
for i in range(a, 0, -1):
    # print(i)
    for _ in range(i):
        for _ in range(i):
            print('*', end='')
        print(' ', end = '')
    print()

# 별찍기 예제 2
a = int(input())
for i in range(a, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(2, a+1):
    for j in range(i):
        print('*', end='')
    print()

# 별찍기 예제 3
a = int(input())
for _ in range(a):
    print('*', end='')
print()
for _ in range(a-2):
    print('*', end='')
    for _ in range(a-2):
        print(' ', end='')
    print('*', end='')
    print()
for _ in range(a):
    print('*', end='')



