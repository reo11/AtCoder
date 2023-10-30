x = int(input())

# 桁は増えない
ans = ""
if x <= 99:
    ans = str(x)
else:
    # なるべく上の桁を編集せずに等差数にする
    # 実現できない場合は、上位の桁を1増やす
    num = x
    while True:
        num_str = list(map(int, list(str(num))))
        a = num_str[0] - num_str[1]
        flag = True
        for i in range(len(num_str) - 1):
            if not flag:
                break
            expected_num = num_str[i] - a
            if expected_num != num_str[i+1]:
                if num_str[i+1] < expected_num and expected_num <= 9 and expected_num >= 0:
                    num_str[i+1] = expected_num
                    for j in range(i+2, len(num_str)):
                        num_str[j] = 0
                else:
                    flag = False
                    if num_str[1] == 9:
                        num_str[0] += 1
                        for j in range(1, len(num_str)):
                            num_str[j] = 0
                    else:
                        num_str[1] += 1
                        for j in range(2, len(num_str)):
                            num_str[j] = 0
                    break
            else:
                continue

        if flag:
            ans = "".join(map(str, num_str))
            break
        else:
            num = int("".join(map(str, num_str)))
print("".join(ans))
