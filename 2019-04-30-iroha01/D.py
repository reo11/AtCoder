n, x, y = map(int, input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)

# takahashi
for v in a[::2]:
    x += v

# Aoki
for v in a[1::2]:
    y += v

if x > y:
    print("Takahashi")
elif x < y:
    print("Aoki")
else:
    print("Draw")