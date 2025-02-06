# sol 1 - 딕셔너리 사용
def solution(participant, completion):
    d = dict()
    for p in participant:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    for c in completion:
        d[c] -= 1
        if d[c] == 0:
            del d[c]
    answer = list(d.keys())[0]
    return answer

# sol 2 - collections 사용 (collections 객체는 차집합 연산이 가능하다)
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]