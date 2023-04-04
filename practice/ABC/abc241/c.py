def solve():
    n = int(input())
    s = []
    for i in range(n):
        s_i = list(input().rstrip())  # 文字に分解
        s.append(s_i)

    BLACK = "#"
    WHITE = "."
    # 横、縦、斜めで舐める
    flag = False

    # 横
    for i in range(n):
        s_length = 0  # 長さが6になるか
        s_black = 0  # 黒の数（4以上でクリア）

        for j in range(n):
            if s[i][j] == BLACK:
                s_black += 1

            if s_length < 6:
                s_length += 1
            elif s_length > 6:
                if s[i][j - 6] == BLACK:
                    s_black -= 1

            if s_black >= 4 and s_length >= 6:
                flag = True
                break
        if flag:
            break

    if flag:
        print("Yes")
        return

    # 縦
    for i in range(n):
        s_length = 0  # 長さが6になるか
        s_black = 0  # 黒の数（4以上でクリア）

        for j in range(n):
            if s[i][j] == BLACK:
                s_black += 1

            if s_length < 6:
                s_length += 1
            elif s_length > 6:
                if s[i][j - 6] == BLACK:
                    s_black -= 1

            if s_black >= 4 and s_length >= 6:
                flag = True
                break
        if flag:
            break

    if flag:
        print("Yes")
        return
    else:
        print("No")
        return


solve()
