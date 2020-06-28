sx, sy, tx, ty = map(int, input().split())

out = ""
def p(s):
    global out
    out += s
# 1回目 行き
for i in range(ty-sy):
    p("U")
for i in range(tx-sx):
    p("R")

# 1回目 帰り
for i in range(ty-sy):
    p("D")
for i in range(tx-sx):
    p("L")

# 2回目 行き
p("L")
for i in range(ty-sy+1):
    p("U")
for i in range(tx-sx+1):
    p("R")
p("D")
# 2回目 帰り
p("R")
for i in range(ty-sy+1):
    p("D")
for i in range(tx-sx+1):
    p("L")
p("U")
print(out)