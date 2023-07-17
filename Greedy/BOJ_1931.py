# 그리디 알고리즘 - 1931번 - 회의실 배정
import sys
N = int(sys.stdin.readline())
time=[]

# 회의 시작&끝나는 시간 입력받기
for i in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))
time.sort(key=lambda x: (x[1], x[0]))
cnt=1
lastEnd=time[0][1]
del time[0]

while len(time)>0:
    if time[0][0]<lastEnd:
        del time[0]
    else:
        lastEnd=time[0][1]
        cnt+=1
        del time[0]
print(cnt)