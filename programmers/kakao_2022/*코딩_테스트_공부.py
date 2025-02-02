import sys

sys.setrecursionlimit(10 ** 5)


def back_tracking(answer, study, cost_sum, alp, cop, problems):
    # problems 탐색 : 풀 수 있는 문제가 생겼는지 확인
    idx = 0
    for p in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = p
        if alp >= alp_req and cop >= cop_req:
            problems.pop(idx)
            idx -= 1
            study.append((alp_rwd, cop_rwd, cost))
            remain -= 1
        idx += 1

    # base condition
    if len(problems) == 0:  # 아직 못 푼 문제들 수
        print(f'>>>>> answer={answer}')
        answer = min(answer, cost_sum)
        return

    # 공부하기
    for (alp_rwd, cop_rwd, cost) in study:
        # print(f'alp_rwd={alp_rwd}, cop_rwd={cop_rwd}, cost={cost}')
        back_tracking(answer, study, cost_sum + cost, alp + alp_rwd, cop + cop_rwd, problems)


def solution(alp, cop, problems):
    study = []
    study.append((1, 0, 1))  # 순서대로 alp_rwd, cop_rwd, cost 시간
    study.append((0, 1, 1))

    ans = float('inf')
    back_tracking(ans, study, 0, alp, cop, problems)

    return ans