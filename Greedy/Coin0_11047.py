# 1. N종류의 동전을 리스트에 저장
# 큰 수부터 확인 -> K보다 작은 동전이 나올 때부터 연산시작
N, K = map(int, input().split())
arr=[]
cnt=0

for i in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)

for i in arr:
    if(K==0):
        break
    if(i<=K):
        cnt+=K//i
        K%=i
print(cnt)