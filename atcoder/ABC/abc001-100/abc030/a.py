a = list(map(int, input().split()))

ta = a[1] / a[0]
ao = a[3] / a[2]

if ta > ao:
    print("TAKAHASHI")
elif ao > ta:
    print("AOKI")
else:
    print("DRAW")