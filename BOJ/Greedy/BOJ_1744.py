# 그리디 알고리즘 - 1744번 - 수 묶기
## 음수&0 // 양수 를 따로 계산하는 것이 포인트!!!
## 모든 수를 묶고나서, (곱했을 때 값) > (그냥 더한 값) 인지 확인하기
## 음수가 있다!!! -> 음수끼리 곱하는게 베스트 -> 0이랑 곱하기 -> 그냥 더하기
import sys
N = int(sys.stdin.readline())
arrMinus = []
arrPlus = []
answer = 0
for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp<=0:
        arrMinus.append(tmp)
    else:
        arrPlus.append(tmp)
arrMinus.sort()
arrPlus.sort(reverse=True)
while len(arrMinus)>1:
    if arrMinus[0]*arrMinus[1] > arrMinus[0]+arrMinus[1]:
        answer += arrMinus[0]*arrMinus[1]
        del arrMinus[0:2]
    else:
        answer += arrMinus[0]
        del arrMinus[0]
if len(arrMinus)==1:
    answer+=arrMinus[0]
while len(arrPlus)>1:
    if arrPlus[0]*arrPlus[1] > arrPlus[0]+arrPlus[1]:
        answer += arrPlus[0] * arrPlus[1]
        del arrPlus[0:2]
    else:
        answer += arrPlus[0]
        del arrPlus[0]
if len(arrPlus)==1:
    answer+=arrPlus[0]
print(answer)