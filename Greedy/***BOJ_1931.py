# 그리디 알고리즘 - 1931번 - 회의실 배정
## 가장 빨리 시작하는 회의 찾기 -> 그 회의 시간과 겹치는 거 다 찾기 -> 그중에서 가장 빨리 끝나는 것 선택하기

N = int(input())
cnt=0
start=[]
end=[]

# 회의 시작&끝나는 시간 입력받기
for i in range(N):
    tmp1, tmp2 = map(int,input().split())
    start.append(tmp1)
    end.append(tmp2)

# 가장 빨리 시작하는 회의 찾기
now = start.index(min(start))
search=[]
# 그 회의랑 겹치는 회의들도 찾기
while(1):
    for i in range(N):
        if (start[now] <= start[i] <= end[now]):
                search.append(end[i])
    if len(search)>0:
        cnt += 1
        nextStart = min(search)     # 다음 회의 시간이 이 시간 이후부터 가능
    # nextStart 보다 큰 start[]중에서 가장 작은값
        # 다음 회의시간 정하기
        minimum=2**32
        for i in start:
            if(i>=nextStart and minimum>i):
                minimum=i
        now = start.index(minimum)
    else:
        break
        # 그 중에서 가장 빨리 끝나는 회의 선택, nowStart=end[빨리끝나는시간)
print(cnt)