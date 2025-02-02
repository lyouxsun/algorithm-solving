def score_check(score, ans, str1, str2):
    if score[str1] > score[str2]:
        ans += str1
    elif score[str1] < score[str2]:
        ans += str2
    else:
        ans += min(str1, str2)
    return ans


def solution(survey, choices):
    n = len(survey)
    score = dict()
    score['R'] = 0
    score['T'] = 0
    score['F'] = 0
    score['C'] = 0
    score['M'] = 0
    score['J'] = 0
    score['A'] = 0
    score['N'] = 0
    for i in range(n):
        if choices[i] < 4:
            score[survey[i][0]] += (4 - choices[i])
        elif choices[i] > 4:
            score[survey[i][1]] += (choices[i] - 4)
        else:
            continue
    ans = score_check(score, '', 'R', 'T')
    ans = score_check(score, ans, 'C', 'F')
    ans = score_check(score, ans, 'J', 'M')
    ans = score_check(score, ans, 'A', 'N')

    return ans