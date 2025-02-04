dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(command):
    answer = [0, 0]
    direction = 0
    for c in command:
        if c == 'R':
            direction = (direction+1) % 4
        elif c == 'L':
            direction = (direction+3) % 4
        elif c == 'G':
            answer[0] += dx[direction]
            answer[1] += dy[direction]
        else:
            answer[0] -= dx[direction]
            answer[1] -= dy[direction]
    # print(answer)
    return answer