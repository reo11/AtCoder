from collections import defaultdict

INF = 10**18
MAX_VALUE = 250002

n, m = map(int, input().split())
a = list(map(int, input().split()))
scores = defaultdict(int)
unsolved = defaultdict(lambda: [])
for i in range(n):
    si = list(input())
    scores[i + 1] = i + 1  # ボーナス点
    for ii, sii in enumerate(si):
        if sii == "o":
            scores[i + 1] += a[ii]
        else:
            scores[i + 1] += 0
            unsolved[i + 1].append(a[ii])
    unsolved[i + 1].sort(reverse=True)

max_score = max(scores.values())
max_score_count = 0
for i in range(n):
    if scores[i + 1] == max_score:
        max_score_count += 1

ans = []
for i in range(n):
    score_i = scores[i + 1]
    if score_i == max_score and max_score_count == 1:
        ans.append(0)
    else:
        ansi = 0
        score = score_i
        for ai in unsolved[i + 1]:
            if max_score > score:
                score += ai
                ansi += 1
            else:
                break
        ans.append(ansi)
print(*ans, sep="\n")
