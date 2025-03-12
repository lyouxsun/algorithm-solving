import heapq

def solution(jobs):
    answer, now, i, start = 0, 0, 0, -1
    heap = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])

        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]
            i += 1
        else:
            now += 1

    return answer // len(jobs)
