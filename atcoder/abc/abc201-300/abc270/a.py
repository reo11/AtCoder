a, b = map(int, input().split())


def solve(score):
    answers = [0, 0, 0]
    if score % 2 == 1:
        answers[0] = 1
        score -= 1

    if score >= 4:
        answers[2] = 4
        score -= 4

    if score == 2:
        answers[1] = 2
    return answers


answers_a = solve(a)
answers_b = solve(b)
ans = 0
for a_i, b_i in zip(answers_a, answers_b):
    ans += max(a_i, b_i)
print(ans)
