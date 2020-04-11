n, k = map(int, input().split())

amount = n**3
center = (k - 1) * (n - k) * 6
center += (k - 1) * 3 + (n - k) * 3
center += 1
print(center / amount)
