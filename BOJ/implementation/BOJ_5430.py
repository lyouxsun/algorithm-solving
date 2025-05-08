# 구현 - 5430번 - AC
import sys
input = sys.stdin.readline

def process_arr(length):
    if length == 0:
        input()
        return list()
    return list(map(int, (input().strip().strip('[]')).split(",")))

def do():
    functions = list(input().strip())
    length = int(input().strip())
    arr = process_arr(length)

    front = True
    for f in functions:
        if f == 'R':
            front = not front
        else:
            if length <= 0:
                print("error")
                return
            length -= 1
            if front:
                arr.pop(0)
            else:
                arr.pop(-1)
    if not front:
        arr.reverse()
    print("[" + ",".join(map(str, arr)) + "]")

cycle = int(input())
for i in range(cycle):
    do()


