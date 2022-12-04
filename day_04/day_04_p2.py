with open("./day_04.in") as fin:
    lines = fin.read().strip().split()


ans = 0
for line in lines:
    elves = line.split(",")
    ranges = [list(map(int, elf.split("-"))) for elf in elves]

    a, b = ranges[0]
    c, d = ranges[1]

    if not (b < c or a > d):
        ans += 1


print(ans)
