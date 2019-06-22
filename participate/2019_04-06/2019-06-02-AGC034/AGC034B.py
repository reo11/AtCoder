s = str(input())

# BC = Dとする
AD_s = ""
index = 0
while index < len(s):
    if s[index:index+2] == "BC":
        AD_s += "D"
        index += 1
    else:
        AD_s += s[index]
    index += 1
# 部分文字列を抽出(BとCで区切られる)
index = 0
l = []
s_part = ""
while index < len(AD_s):
    if AD_s[index] == "B" or AD_s[index] == "C" or index == len(AD_s) - 1:
        if index == len(AD_s) - 1:
            s_part += AD_s[index]
        if s_part != "":
            l.append(s_part)
            s_part = ""
    else:
        s_part += AD_s[index]
    index += 1

ans = 0

for part in l:
    # ADADとか
    d_count = 0
    for i, c in enumerate(list(part)):
        if c == "D":
            ans += i - d_count
            d_count += 1

print(ans)
