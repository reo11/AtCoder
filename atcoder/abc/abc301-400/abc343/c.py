n = int(input())

def is_mirror(x):
    return x == x[::-1]

ans = 1
for i in range(2, n):
    ans_cand = i ** 3
    if ans_cand <= n:
        if is_mirror(str(ans_cand)):
            ans = ans_cand
    else:
        break
print(ans)