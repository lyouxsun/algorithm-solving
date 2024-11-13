# DP - 2775번 - 부녀회장이 될테야
t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y+1]))
        people = new.copy()
        # print(people)
    print(people[-1])