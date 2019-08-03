h, w = map(int, input().split())
c = [str(input()) for _ in range(h)]

for i in range(h*2):
    print(c[i//2])
