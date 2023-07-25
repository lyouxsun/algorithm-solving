# 그리디 알고리즘 - 1202번 - 보석 도둑
## 배열에 가방 무게&가격 입력받기 -> 우선순위큐에 가방 무게 입력받기 -> 가방 개수만큼 가능한
import heapq
import sys
jewelNum, bagNum = map(int, sys.stdin.readline().split())
jewels = []
bags = []
answer = 0
for i in range(jewelNum):
    jewels.append(list(map(int, sys.stdin.readline().split())))
for i in range(bagNum):
    bags.append(int(sys.stdin.readline()))
bags.sort()
jewels.sort(key=lambda x:(-x[1], x[0]))
# 우선순위 큐에 삽입 할 때, 가격이 비싼 보석이 최대가 되도록?
tmp = []
for i in bags:
    while jewels and i>=jewels[0][0]:
        heapq.heappush(tmp, -jewels[0][1])
        heapq.heappop(jewels)
    if tmp:
        answer -= heapq.heappop(tmp)
print(answer)
'''
# i보다 작거나 같은 보석 중 가장 비싼 보석을 heap에서 pop하면 됨
# 최대힙 (가격이 비싼 보석이 루트노드)
for j in range(len(jewels)):
    if jewels[j][0]<=i:
        heapq.heappush(tmp, -jewels[j][1])
    tmp = heapq.heappop(tmp)
    answer -= tmp
jewels.remove(tmp)
'''