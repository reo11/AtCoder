n = int(input())
x = 0
y = 0

for i in range(n):
    xi, yi = map(int, input().split())
    x += xi
    y += yi

if x > y:
    print("Takahashi")
elif x < y:
    print("Aoki")
else:
    print("Draw")
