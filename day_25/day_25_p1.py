with open("./day_25.in") as fin:
    lines = fin.read().strip().split()

# String to digit
s2d = {
    "0": 0,
    "1": 1,
    "2": 2,
    "-": -1,
    "=": -2
}

d2s = {d: s for s, d in s2d.items()}


def parse_snafu(s):
    ans = 0
    d = len(s)
    p = 1
    s = s[::-1]
    for i in range(d):
        ans += p * s2d[s[i]]
        p *= 5
    return ans


ans = 0
for line in lines:
    ans += parse_snafu(line)


def int_to_snafu(n):
    res = ""
    while n > 0:
        d = ((n + 2) % 5) - 2
        res += d2s[d]
        n -= d
        n //= 5
    return res[::-1]


print(int_to_snafu(ans))
