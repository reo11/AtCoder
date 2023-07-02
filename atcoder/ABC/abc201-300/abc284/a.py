n = int(input())
s = []
for _ in range(n):
    s_i = input()
    s.append(s_i)
s = s[::-1]
print(*s, sep='\n')