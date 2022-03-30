s = str(input())

is_yymm = False
is_mmyy = False

if 0 < int(s[:2]) < 13:
    is_mmyy = True
if 0 < int(s[2:4]) < 13:
    is_yymm = True

ans = ""
if is_yymm and not is_mmyy:
    ans = "YYMM"
elif is_mmyy and not is_yymm:
    ans = "MMYY"
elif is_yymm and is_mmyy:
    ans = "AMBIGUOUS"
else:
    ans = "NA"
print(ans)