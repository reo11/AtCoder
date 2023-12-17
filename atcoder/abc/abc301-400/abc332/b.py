k, g, m = map(int, input().split())

glass = 0
cup = 0

for _ in range(k):
    if glass == g:
        glass = 0
    elif cup == 0:
        cup = m
    else:
        glass += cup
        cup = 0
        if glass > g:
            cup = glass - g
            glass = g
print(glass, cup)