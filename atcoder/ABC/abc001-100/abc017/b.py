x = str(input())
x = x.replace("ch", "").replace("o", "").replace("k", "").replace("u", "")
if x == "":
    print("YES")
else:
    print("NO")
