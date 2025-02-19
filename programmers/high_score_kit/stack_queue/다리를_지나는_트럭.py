# bridge_length : 다리에 올라갈 수 있는 최대 트럭 수
# weight : 다리가 견딜 수 있는 최대 무게 (다리에 완전히 오르지 않은 트럭의 무게는 무시)
# 큐
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    n = len(truck_weights)
    bridge = deque()
    bridge.append([truck_weights[0], 0])
    next = 1
    now_weight = truck_weights[0]
    # print(answer, bridge)

    while bridge:
        # print(answer, bridge)
        answer += 1
        for i in range(len(bridge)):
            bridge[i][1] += 1
        if bridge[0][1] >= bridge_length:
            truck_weight, cnt = bridge.popleft()
            now_weight -= truck_weight
        if next < n:
            if now_weight + truck_weights[next] <= weight:
                bridge.append([truck_weights[next], 0])
                now_weight += truck_weights[next]
                next += 1

    return answer
