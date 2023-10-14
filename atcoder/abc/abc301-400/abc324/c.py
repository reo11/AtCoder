from collections import deque
n, t = input().split()
n = int(n)
s = [input() for _ in range(n)]

def create_correct_set(t):
    correct_set = set()
    # 1
    correct_set.add(t)

    # 2
    for pos in range(n + 1):
        for alph in range(26):
            correct_set.add(t[:pos] + chr(ord('a') + alph) + t[pos:])

    # 3
    for pos in range(n):
        # O(n**2)
        correct_set.add(t[:pos] + t[pos + 1:])

    # 4
    for pos in range(n):
        for alph in range(26):
            # O(n**2)
            correct_set.add(t[:pos] + chr(ord('a') + alph) + t[pos + 1:])
    return correct_set


def solve1(n, t, s):
    ans = []
    correct_set = create_correct_set(t)
    for i in range(n):
        if s[i] in correct_set:
            ans.append(i + 1)
    return ans

def leavenshtain_distance(s1, s2):
    cnt = 0
    for si1, si2 in zip(s1, s2):
        if si1 != si2:
            cnt += 1
    return cnt

def solve2(n, t, s):
    # 都度確認する
    # まずあり得る長さはt+-1
    ans = []
    for i, si in enumerate(s, 1):
        if len(si) < len(t) - 1 or len(si) > len(t) + 1:
            continue
        # 長さが同じ場合
        if len(si) == len(t):
            if si == t:
                ans.append(i)
            elif leavenshtain_distance(si, t) == 1:
                ans.append(i)
            continue
        elif len(si) == len(t) - 1:
            queue_s = deque(list(si))
            queue_t = deque(list(t))
            # 1文字削除を許容
            cnt = 0
            while queue_s and queue_t:
                si1 = queue_s.popleft()
                ti1 = queue_t.popleft()
                if si1 != ti1:
                    if cnt == 0:
                        cnt += 1
                        if queue_t:
                            ti1 = queue_t.popleft()
                            if si1 != ti1:
                                cnt += 1
                                break
                            else:
                                continue
                        else:
                            break
                    else:
                        cnt += 1
                        break
            if cnt <= 1:
                ans.append(i)
        elif len(si) == len(t) + 1:
            queue_s = deque(list(si))
            queue_t = deque(list(t))
            # 1文字追加を許容
            cnt = 0
            while queue_s and queue_t:
                si1 = queue_s.popleft()
                ti1 = queue_t.popleft()
                if si1 != ti1:
                    if cnt == 0:
                        cnt += 1
                        if queue_s:
                            si1 = queue_s.popleft()
                            if si1 != ti1:
                                cnt += 1
                                break
                            else:
                                continue
                        else:
                            break
                    else:
                        cnt += 1
                        break
            if cnt <= 1:
                ans.append(i)
        else:
            continue
    return ans

# ans = solve1(n, t, s)
ans = solve2(n, t, s)
print(len(ans))
print(*ans, sep=" ")