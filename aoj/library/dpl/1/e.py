s1 = str(input())
s2 = str(input())


def levenshtein_distance(s1: str, s2: str):
    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp


print(levenshtein_distance(s1, s2))
