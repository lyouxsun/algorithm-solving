# 그리디 알고리즘 - 1541번 - 잃어버린 괄호
## (-)를 받았을 때, 그 뒤의 수가 최대가 되도록 괄호로 묶어주면 된다. -> (-)로만 쪼개주면 되는거임

str = input()
arr=[]
answer = 0

for i in str.split('-'):
    arr.append(i)

for i in arr[0].split('+'):
    answer += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        answer -= int(j)
print(answer)