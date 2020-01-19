import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = []
for i in range(n):
    ab.append([a[i], b[i]])

pat1 = []; pat2 = []
for i in range(n):
    pat1.append((ab[i][i % 2], i))
    pat2.append((ab[i][(i+1) % 2], i))
pat1.sort()
pat2.sort()
print(pat1, pat2)

