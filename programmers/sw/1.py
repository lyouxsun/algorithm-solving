def solution(a, b):
    b = list(set(b))
    # print('b =', b)

    for _ in range(3):
        if len(a) == 0:
            break

    # 1단계
    plus = []
    for i in range(len(a)):
        if a.count(a[i]) == 1:
            plus.append(i)

    for p in plus:
        a[p] += 1

    # 2단계
    new_a = []
    for i in a:
        if i not in b:
            new_a.append(i)
        a = new_a
    # print(a)
    # print()

    return a