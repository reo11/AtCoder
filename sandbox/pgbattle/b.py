s = list(input())

ans = 0
abc = list("ABC")
for i in range(len(s) - 2):
    count = 0
    count_question = 0
    for j in range(3):
        if s[i + j] == abc[j]:
            count += 1
        elif s[i + j] == "?":
            count += 1
            count_question += 1
    if count == 3:
        ans += 3**-count_question

print(ans)
