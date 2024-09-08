# 자료구조(스택) - 11899번 - 괄호 끼워넣기
string = list(input().strip())
s = []
ans = 0
for i in string:
    if len(s) == 0 or i == '(':
        s.append(i)
    elif s[-1] != '(' and i == ')':
        s.append(i)
    elif s[-1] == '(' and i == ')':
        s.pop()
# print(s)
print(len(s))