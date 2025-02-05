from heapq import heapify, heappush, heappop

def solution(ability, number):
    heapify(ability)
    for _ in range(number):
        a = heappop(ability)
        b = heappop(ability)
        heappush(ability, a+b)
        heappush(ability, a+b)
    return sum(ability)