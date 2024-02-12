hw = list(map(int, input().split()))
# ii, ij, ji, jjを全探索

def check(ii, ij, ik, ji, jj, jk, ki, kj, kk):
    for x in [ii, ij, ik, ji, jj, jk, ki, kj, kk]:
        if x <= 0:
            return False
    if ii + ij + ik != hw[0]:
        return False
    if ji + jj + jk != hw[1]:
        return False
    if ki + kj + kk != hw[2]:
        return False
    if ii + ji + ki != hw[3]:
        return False
    if ij + jj + kj != hw[4]:
        return False
    if ik + jk + kk != hw[5]:
        return False
    return True

ans = 0
for ii in range(1, max(hw[0], hw[3]) - 1):
    for ij in range(1, min(hw[0] - ii, hw[4])):
        for ji in range(1, min(hw[1], hw[3] - ii)):
            for jj in range(1, min(hw[4] - ij, hw[1] - ji)):
                ik = hw[0] - ii - ij
                jk = hw[1] - ji - jj
                ki = hw[3] - ii - ji
                kj = hw[4] - ij - jj
                kk = hw[5] - ik - jk
                flag = True
                if check(ii, ij, ik, ji, jj, jk, ki, kj, kk):
                    ans += 1
print(ans)