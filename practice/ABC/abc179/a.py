s = str(input())

ans = ""
if s[-1] == "s":
    ans = s + "es"
else:
    ans = s + "s"
print(ans)