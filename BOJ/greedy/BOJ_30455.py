# 그리디 - 30455번 - 이제는 더 이상 물러날 곳이 없다
import sys

input = sys.stdin.readline

n = int(input())
duck = 0
goose = n - 1

while True:
    if duck + 1 == goose:
        print('Duck')
        break
    duck += 1

    if goose - 1 == duck:
        print('Goose')
        break
    goose -= 1
