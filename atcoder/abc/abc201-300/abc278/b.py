def valid(a, b, c, d):
    ab = str(a) + str(b)
    cd = str(c) + str(d)
    if int(ab) >= 0 and int(ab) <= 23 and int(cd) >= 0 and int(cd) <= 59:
        return True
    else:
        return False

h, m = map(int, input().split())
for i in range(60 * 24):
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    h_str = str(h)
    if len(h_str) == 1:
        h_str = "0" + h_str
    m_str = str(m)
    if len(m_str) == 1:
        m_str = "0" + m_str
    if valid(h_str[0], m_str[0], h_str[1], m_str[1]):
        print(h_str, m_str)
        exit()
    m += 1
