sa = str(input())
sb = str(input())
sc = str(input())

ia = 0
ib = 0
ic = 0

turn = "a"
winner = ""
while True:
    if turn == "a":
        if ia >= len(sa):
            winner = "A"
            break
        turn = sa[ia]
        ia += 1
    elif turn == "b":
        if ib >= len(sb):
            winner = "B"
            break
        turn = sb[ib]
        ib += 1
    else:
        if ic >= len(sc):
            winner = "C"
            break
        turn = sc[ic]
        ic += 1
print(winner)