from heapq import *

def solution(s, K):
    heapify(s)
    answer = 0

    while s[0] < K:
        if len(s) < 2:
            return -1
        num1 = heappop(s)
        num2 = heappop(s)
        new_num = num1 + 2 * num2
        heappush(s, new_num)
        # print(s)
        answer += 1
    return answer