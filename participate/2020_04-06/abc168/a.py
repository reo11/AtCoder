n = int(input())
ans = "bon"
if n % 10 in [2, 4, 5, 7, 9]:
    ans = "hon"
elif n % 10 in [0, 1, 6, 8]:
    ans = "pon"
print(ans)