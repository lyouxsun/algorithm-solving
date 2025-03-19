import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    answer = []

    for operation in operations:
        flag, value = operation.split()
        value = int(value)
        if operation[0] == "I":
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, value * -1)
        elif operation[0] == "D" and min_heap:
            if value == 1:
                heapq.heappop(max_heap)
                min_heap = []
                for member in max_heap:
                    heapq.heappush(min_heap, member * -1)
            elif value == -1:
                heapq.heappop(min_heap)
                max_heap = []
                for member in min_heap:
                    heapq.heappush(max_heap, member * -1)

    if min_heap:
        answer.append(max(min_heap))
        answer.append(min(min_heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer
