n = int(input())
a = list(map(int, input().split()))

p = 1
for ai in a:
    p *= ai

if p > 0:
    print("+")
elif p == 0:
    print("0")
else:
    print("-")