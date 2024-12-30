s = input()
counts = [0, 0]
small_alphabets = [chr(i) for i in range(97, 97+26)]

for si in list(s):
    if si in small_alphabets:
        counts[0] += 1
    else:
        counts[1] += 1

if counts[0] > counts[1]:
    print(s.lower())
else:
    print(s.upper())
