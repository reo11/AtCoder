k = int(input())

h = k // 60
m = k % 60
h += 21
if m <= 9:
    m = '0' + str(m)
print(f"{h}:{m}")
