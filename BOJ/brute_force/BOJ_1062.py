# 완전탐색 - 1062번 - 가르침
import sys
from itertools import combinations

input = sys.stdin.readline
N, K = map(int, input().split())

# a, n, t, i, c는 반드시 가르쳐야 하므로, 5보다 작으면 단어를 읽을 수 없음
if K < 5:
    print(0)
    sys.exit(0)
# 모든 알파벳을 배웠다면 모든 단어를 읽을 수 있음
if K == 26:
    print(N)
    sys.exit(0)

K -= 5  # 필수 알파벳 5개를 뺌
words = []
learned = [False] * 26
for ch in ['a', 'n', 't', 'i', 'c']:
    learned[ord(ch) - ord('a')] = True
candidates = set()
pre_read_count = 0
for _ in range(N):
    word = input().strip()[4:-4]  # anta, tica 제거
    if not word:
        pre_read_count += 1
        continue
    words.append(word)
    for ch in word:
        candidates.add(ch)

# 이미 배운 5개 제거
candidates -= {'a', 'n', 't', 'i', 'c'}

# 후보 알파벳 수가 K 이하라면 모든 단어를 읽을 수 있음
if len(candidates) <= K:
    print(N)
    sys.exit(0)

## 주의!!! 만약, exist_alphabet 배열의 크기가 K보다 작으면 comb는 빈 배열이 된다!
max_read = 0
for comb in combinations(candidates, K):        # 집합도 올 수 있음
    for ch in comb:
        learned[ord(ch) - ord('a')] = True
    count = 0
    for word in words:
        if all(learned[ord(ch) - ord('a')] for ch in word):
            count += 1
    max_read = max(max_read, count)
    for ch in comb:
        learned[ord(ch) - ord('a')] = False

print(max_read + pre_read_count)
