n = int(input())
ans = float("inf")
for num in range(n, 1000):
    num_str = str(num)
    num_str = "0" * (3 - len(num_str)) + num_str
    if len(num_str) == 3:
        if int(num_str[0]) * int(num_str[1]) == int(num_str[2]):
            ans = min(ans, num)
print(ans)