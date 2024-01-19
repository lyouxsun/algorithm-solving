# list comprehension : 선언과 동시에 for loop으로 부터 나온 원소를 원하는 값으로 변경해줄 수 있다.

arr = [1, 2, 3, 5]

# v1
new_arr = []
for elem in arr:
    new_arr.append(elem * 2)

# v2. list comprehension
## [(append 안에 들어갈 내용) (for loop)]
new_arr = [elem * 2 for elem in arr]

## [(append 안에 들어갈 내용) (for loop) <조건문>]