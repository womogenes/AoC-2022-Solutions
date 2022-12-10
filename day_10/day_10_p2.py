with open("./day_10.in") as fin:
    lines = fin.read().strip().split("\n")

cur_X = 1
op = 0
ans = 0

row = 0
col = 0

X = [1] * 241

for line in lines:
    parts = line.split(" ")

    if parts[0] == "noop":
        op += 1
        X[op] = cur_X

    elif parts[0] == "addx":
        V = int(parts[1])

        X[op + 1] = cur_X
        cur_X += V

        op += 2
        X[op] = cur_X


# Ranges from [1, 39]
ans = [[None] * 40 for _ in range(6)]

for row in range(6):
    for col in range(40):
        counter = row * 40 + col + 1
        if abs(X[counter - 1] - (col)) <= 1:
            ans[row][col] = "##"
        else:
            ans[row][col] = "  "


for row in ans:
    print("".join(row))
