# 그리디 알고리즘 - 16953번 - A->B
import sys
start, end = map(int, sys.stdin.readline().split())
checkEnd = end
cnt = 1
while True:
    checkEnd = end
    if end == start:
        print(cnt)
        cnt = -1
        break
    elif end < start:
        break
    elif end % 2 == 0:
        end //= 2
        cnt += 1
    elif str(end)[-1] == '1':
        end = int(end)//10
        cnt += 1
    elif end == checkEnd:
        break
if cnt != -1:
    print('-1')