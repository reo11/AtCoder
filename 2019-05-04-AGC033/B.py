from collections import defaultdict
s_dict = defaultdict(lambda: 0)
t_dict = defaultdict(lambda: 0)

h, w, n = map(int, input().split())
sr, sc = map(int, input().split())
s = list(str(input()))
t = list(str(input()))

for i in range(n):
    s_dict[s[i]] += 1
    t_dict[t[i]] += 1

# 落ちるパターン
# 駒が端にあり、高橋くんが場外に移動させることができる場合、落ちる
ans = "NO"
first = False
if sr == 1 and s_dict["L"] > 0 or sr == w and s_dict["R"] > 0 or sc == 1 and s_dict["U"] > 0 or sc == h and s_dict["D"] > 0:
    first = True

s_sum = defaultdict(lambda: 0)
t_sum = defaultdict(lambda: 0)
if not first:
    # それぞれの累積和でmaxを考える
    for i in range(n):
        s_sum[s[i]] += 1
        # 高橋くんは落とさないようにする制約がある
        # 何もしないこともある
        if t[i] == "L" and t_sum["L"] + 1 - s_sum["R"] > sr - 1:
            pass
        elif t[i] == "R" and t_sum["R"] + 1 - s_sum["L"] > w - sr:
            pass
        elif t[i] == "U" and t_sum["U"] + 1 - s_sum["D"] > sc - 1:
            pass
        elif t[i] == "D" and t_sum["D"] + 1 - s_sum["U"] > h - sc:
            pass
        else:
            t_sum[t[i]] += 1

        if sr <= s_sum["L"] - t_sum["R"]:
            break
        elif w - sr < s_sum["R"] - t_sum["L"]:
            break
        elif sc <= s_sum["U"] - t_sum["D"]:
            break
        elif h - sc < s_sum["D"] - t_sum["U"]:
            break
        if i == n-1:
            ans = "YES"
print(ans)

