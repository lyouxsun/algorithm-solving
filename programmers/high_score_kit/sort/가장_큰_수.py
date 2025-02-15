def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    print(numbers)

    for i in numbers:
        answer += i

    return answer
