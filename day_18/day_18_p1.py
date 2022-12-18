import numpy as np

with open("./day_18.in") as fin:
    lines = fin.read().strip().split("\n")

filled = set()
for line in lines:
    x, y, z = map(int, line.split(","))
    filled.add((x, y, z))


ans = 0
for x, y, z in filled:
    covered = 0

    pos = np.array((x, y, z))

    for coord in range(3):
        dpos = np.array([0, 0, 0])
        dpos[coord] = 1

        dneg = np.array([0, 0, 0])
        dneg[coord] = -1

        covered += tuple(pos + dpos) in filled
        covered += tuple(pos + dneg) in filled

    ans += 6 - covered

print(ans)
