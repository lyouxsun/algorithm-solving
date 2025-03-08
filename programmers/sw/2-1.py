def find(board, word):
    value = 0
    now = 0
    for i in range(len(word)):
        want = word[i]
        next = board.index(word[i])
# print('want=', want)
# print('next=', next)
# print('now=', now)
    value += abs(now - next)
# print('value=', abs(now-next))
    now = next
    return value


def solution(s, words):
    board = list(s)
    answers = []
    for i in range(0, len(words)):
        answer = find(board, words[i])
        answers.append(answer)
    return answers
