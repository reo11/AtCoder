n = int(input())

ans = "Bad"
if n == 100:
    ans = "Perfect"
elif 90 <= n <= 99:
    ans = "Great"
elif 60 <= n <= 89:
    ans = "Good"

print(ans)
