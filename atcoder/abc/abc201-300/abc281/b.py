s = list(input())

if len(s) == 8:
    try:
        i = s[0]
        j = int("".join(s[1:-1]))
        k = s[-1]
        assert i in [chr(ord("A") + i) for i in range(26)]
        assert k in [chr(ord("A") + i) for i in range(26)]
        assert j >= 10**5 and j < 10**6
        print("Yes")
    except:
        print("No")
else:
    print("No")