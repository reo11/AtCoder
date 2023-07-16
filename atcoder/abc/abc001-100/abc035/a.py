w, h = map(int, input().split())

if int(w / h * 9) == 12:
    print("4:3")
else:
    print("16:9")
