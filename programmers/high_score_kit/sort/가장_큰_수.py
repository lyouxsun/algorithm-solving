
def solution(numbers):
    answer = ''
    num = list(map(str, numbers))
    s = sorted(num ,key=lambda x: x* 3, reverse=True)
    answer += ''.join(s)
    return str(int(answer))
