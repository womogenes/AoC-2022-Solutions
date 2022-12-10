with open("./day_10.in") as fin:
    lines = fin.read().strip().split("\n")

X = 1
op = 0

ans = 0
interesting = [20, 60, 100, 140, 180, 220]

for line in lines:
    parts = line.split(" ")

    if parts[0] == "noop":
        op += 1

        if op in interesting:
            ans += op * X

    elif parts[0] == "addx":
        V = int(parts[1])
        X += V

        op += 1

        if op in interesting:
            ans += op * (X - V)

        op += 1

        if op in interesting:
            ans += op * (X - V)


print(ans)
