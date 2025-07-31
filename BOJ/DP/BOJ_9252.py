# DP - 9252번 - LCS 2
import sys

input = sys.stdin.readline
str1 = list(input().strip())
str2 = list(input().strip())
len1, len2 = len(str1), len(str2)
# dp[i][j] = str1[:i]과 str2[:j] 의 LCS 길이
dp = [[0] * len2 for _ in range(len1)]
lcs = [[''] * len2 for _ in range(len1)]

# 1. dp[0][j], dp[i][0] 다 채우기
for i in range(len1):
    if str2[0] in str1[:i+1]:
        dp[i][0] = 1
        lcs[i][0] = str2[0]
        ans = 1
    else:
        dp[i][0] = 0

for j in range(len2):
    if str1[0] in str2[:j+1]:
        dp[0][j] = 1
        lcs[0][j] = str1[0]
        ans = 1
    else:
        dp[0][j] = 0

# 2. 이전것들과 비교하며 채우기
for i in range(1, len1):
    for j in range(1, len2):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if i < j:
                lcs[i][j] = str(lcs[i - 1][j - 1]) + str(str1[i])
            else:
                lcs[i][j] = str(lcs[i - 1][j - 1]) + str(str2[j])
        else:
            # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                lcs[i][j] = str(lcs[i - 1][j])
            else:
                dp[i][j] = dp[i][j - 1]
                lcs[i][j] = str(lcs[i][j - 1])

ans, ans_lcs = 0, ''
for i in range(len1):
    for j in range(len2):
        if ans < dp[i][j]:
            ans = dp[i][j]
            ans_lcs = lcs[i][j]
# print(dp)
# print(lcs)
print(ans)
if ans != 0:
    print(ans_lcs)

# 반례 : 답은 4, ACAK
# CAPCAK
# ACAYKP
