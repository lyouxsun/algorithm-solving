# DP - 9252번 - LCS 2
import sys

input = sys.stdin.readline
str1 = list(input().strip())
str2 = list(input().strip())

dp = [[0] * 2 for _ in range(len(str1))]
lcs = ['' for _ in range(len(str1))]

for s1 in range(len(str1)):  # s1 : str1 의 인덱스, dp 테이블의 기준 인덱스
    if s1 == 0 or all(dp[i][0] for i in range(len(str1))) == 0:
        for i in range(len(str2)):
            if str2[i] == str1[s1]:
                dp[s1][0] = 1
                dp[s1][1] = i
                lcs[s1] = str(str2[i])
                break
    for l in range(s1):  # l : dp[s1]
        last = dp[l][1]
        for i in range(last + 1, len(str2)):
            if str2[i] == str1[s1]:
                if dp[s1][0] < dp[l][0] + 1:
                    dp[s1][0] = dp[l][0] + 1
                    dp[s1][1] = i
                    lcs[s1] = str(lcs[l]) + str(str2[i])
                    break

# print(dp)
# print(lcs)

dp2 = [[0] * 2 for _ in range(len(str2))]
lcs2 = ['' for _ in range(len(str2))]

for s2 in range(len(str2)):  # s1 : str1 의 인덱스, dp 테이블의 기준 인덱스
    if s2 == 0 or all(dp[i][0] for i in range(len(str2))) == 0:
        for i in range(len(str1)):
            if str1[i] == str2[s2]:
                dp2[s2][0] = 1
                dp2[s2][1] = i
                lcs2[s2] = str(str1[i])
                break
    for l in range(s2):  # l : dp[s1]
        last = dp2[l][1]
        for i in range(last + 1, len(str1)):
            if str1[i] == str2[s2]:
                if dp2[s2][0] < dp2[l][0] + 1:
                    dp2[s2][0] = dp2[l][0] + 1
                    dp2[s2][1] = i
                    lcs2[s2] = str(lcs2[l]) + str(str1[i])
                    break
# print(dp2)
# print(lcs2)

ans = 0
ans_lcs = ''
for i in range(len(str1)):
    if dp[i][0] > ans:
        ans = dp[i][0]
        ans_lcs = lcs[i]
    if dp2[i][0] > ans:
        ans = dp2[i][0]
        ans_lcs = lcs2[i]
print(ans)
if ans != 0:
    print(ans_lcs)


# 반례 : 답은 4, ACAK
# CAPCAK
# ACAYKP

