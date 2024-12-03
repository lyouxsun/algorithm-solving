# 해시, 맵 (사실 dictionary 씀) - 1620번 - 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()
for i in range(1, n+1):
    pokemon = input().strip()
    dic[str(i)] = pokemon
    dic[pokemon] = i

for i in range(m):
    print(dic[input().strip()])
