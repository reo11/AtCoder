a, b = map(int, input().split())

if int(a/2) + 1 >= b:
    result = 'YES'
else:
    result = 'NO'
# 出力
print("{}".format(result))