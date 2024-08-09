# 브루트 포스 - 17089번 - 세 친구
## 친구 관계를 그래프(2차원 배열)로 나타내자!

p, r = map(int, input().split())
relations = []
people = [[False] * (p + 1) for i in range(p + 1)]
friends = [0] * (p+1)       # 친구 수 저장하는 배열
for i in range(r):
    relations.append(list(map(int, input().split())))
for i in relations:
    people[i[0]][i[1]] = True
    people[i[1]][i[0]] = True
    friends[i[0]] += 1
    friends[i[1]] += 1

# print(friends)

ans = float('INF')
for i in range(1, p+1):
    for j in range(1, p+1):
        r = 0
        if people[i][j]:  ## i, j가 친구관계인 경우에만 k를 구한다 -> 시간 복잡도가 N**3에서 N**2+M*N 이 된다
            for k in range(1, p+1):
                if people[i][k] and people[j][k]:       # i, j, k 가 같은 수여도 friends에서 걸러지니까 ㄱㅊ
                    r = friends[i] + friends[j] + friends[k] - 6
                    ans = min(ans, r)
if ans == float('INF'):
    print(-1)
else:
    print(ans)
