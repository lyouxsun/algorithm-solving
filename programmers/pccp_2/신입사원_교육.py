from heapq import heappush, heappop, heapify

def solution(ability, number):
    heapify(ability)
    for i in range(number):
        n1, n2 = heappop(ability), heappop(ability)
        heappush(ability, n1+n2)
        heappush(ability, n1+n2)
    # print(ability)
    answer = sum(ability)
    return answer