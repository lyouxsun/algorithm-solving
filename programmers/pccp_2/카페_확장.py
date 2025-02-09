"""
    menu : 각 메뉴의 제조시간
    order : 주문한 음료 (순서대로 정렬되어 있음)
    k : 새로운 한 명의 손님이 방문하는데 걸리는 시간
    answer = 동시에 기다리는 손님 수의 최댓값
"""


def solution(menu, order, k):
    num = len(order)
    answer = 0
    visit = [[0] * 2 for _ in range(num)]
    for i in range(num):
        visit[i][0] = i * k

    last_end = 0
    for i in range(num):
        visit[i][1] = max(last_end, visit[i][0]) + menu[order[i]]
        last_end = visit[i][1]

        cnt = min(num, (last_end - 1) // k + 1) - i
        # print(f'i = {i}, target={last_end}, cnt={cnt}')
        answer = max(answer, cnt)

    print(visit)

    return answer