s = str(input())

if len(s) == 1:
    print(str(s[0].upper()))
else:
    print(str(s[0].upper()) + str(s[1:].lower()))
