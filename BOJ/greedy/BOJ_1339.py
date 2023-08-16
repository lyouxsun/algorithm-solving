# 그리디 알고리즘 - 단어 수학 - 1339번
import sys
N = int(sys.stdin.readline())
inputs = []     # 입력 문자열들의 집합
dict = {}     # 이미 문자->숫자로 변환 완료한 문자들 집합
sum = 0
for i in range(N):
    inputs.append(list(map(str, sys.stdin.readline().strip())))
for i in range(N):
    for j in range(len(inputs[i])):
        tmp = str(inputs[i][j])
        if tmp in dict:
            dict[tmp] = dict[tmp]+10**(len(inputs[i])-j-1)
        else:
            dict[tmp] = 10**(len(inputs[i])-j-1)
arr = sorted(dict.items(), key=lambda x:x[1], reverse=True)
num = 9
for i in range(len(arr)):
    sum += arr[i][1]*num
    num -= 1
print(sum)