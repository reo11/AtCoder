n = int(input())
count_ab = 0
tail_a = 0
head_b = 0
hb_ta = 0
ans = 0
for i in range(n):
    s = str(input())
    if s[0] == "B" and s[-1] == "A":
        hb_ta += 1
    elif s[0] == "B":
        head_b += 1
    elif s[-1] == "A":
        tail_a += 1
    for j in range(len(s) - 1):
        if s[j : j + 2] == "AB":
            count_ab += 1

if tail_a > 0 and head_b > 0:
    ans = 1 + hb_ta
    ans += min(tail_a - 1, head_b - 1)
elif tail_a > 0 or head_b > 0:
    # head_bかtail_aが0の時
    ans = hb_ta
else:
    # どちらも0のとき
    if hb_ta > 0:
        ans = hb_ta - 1
    else:
        ans = 0
ans += count_ab
print(ans)
