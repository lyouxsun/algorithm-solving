import sys

M, D = map(int, input().split())
remain = 0
for i in range(1, 13):
    if i == M:
        break
    if i == 2:
        remain += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        remain += 30
    else:
        remain += 31

remain = (remain + D - 1) % 7  # 날짜까지 반영해야 정확함

if remain == 0:
    print("MON")
elif remain == 1:
    print("TUE")
elif remain == 2:
    print("WED") 
elif remain == 3:
    print("THU")
elif remain == 4:
    print("FRI")
elif remain == 5:
    print("SAT")
else:
    print("SUN")