# 약수, 배수와 소수 - 1735번 - 분수 합

N1, N2 = map(int, input().split())
M1, M2 = map(int, input().split())
lcm = N2*M2
# N2, M2의 최소공배수 구하기
a=M2
b=N2
while(b!=0):
    if(a%b==0):
        lcm /= b
        break
    else:
        tmp=a
        a = b
        b = tmp % a
ans1 = lcm//N2*N1 + lcm//M2*M1

b=ans1
a=lcm
while(b!=0):
    if a % b == 0:
        ans1 /= b
        lcm /=b
        break
    else:
        tmp = a
        a = b
        b = tmp % a
print(int(ans1), int(lcm))