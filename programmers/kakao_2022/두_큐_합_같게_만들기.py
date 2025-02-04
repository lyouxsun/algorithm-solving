def solution(queue1, queue2):
    total = []
    total.extend(queue1)
    total.extend(queue2)
    length = len(total)

    total_sum = sum(total)
    if total_sum % 2 == 1:
        return -1
    result = total_sum // 2
    # for i in total:
    #     if i > result:
    #         return -1

    start, end = 0, length // 2 - 1
    answer = 0
    q1_sum = sum(queue1)  # queue1에 대해서만 계산하자!

    while end >= start:
        if q1_sum == result:
            return answer

        if q1_sum > result:
            q1_sum -= total[start]
            start += 1
        else:
            end += 1
            if end >= length:
                return -1
            q1_sum += total[end]

        answer += 1

    return -1