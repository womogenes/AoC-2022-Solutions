import numpy as np
from itertools import product
from functools import lru_cache
from tqdm import tqdm

with open("./day_18.in") as fin:
    lines = fin.read().strip().split("\n")


min_coord = 1 << 60
max_coord = -(1 << 60)

filled = set()
for line in lines:
    x, y, z = map(int, line.split(","))
    filled.add((x, y, z))

    for num in [x, y, z]:
        min_coord = min(min_coord, num)
        max_coord = max(max_coord, num)


# Actually just count if exposed to outside
@lru_cache(None)
def exposed(pos):
    # do a DFS
    stack = [pos]
    seen = set()

    if pos in filled:
        return False

    while len(stack) > 0:
        pop = stack.pop()

        if pop in filled:
            continue

        for coord in range(3):
            if not (min_coord <= pop[coord] <= max_coord):
                return True

        if pop in seen:
            continue
        seen.add(pop)

        for coord in range(3):
            dpos = np.array([0, 0, 0])
            dpos[coord] = 1
            dneg = np.array([0, 0, 0])
            dneg[coord] = -1

            stack.append(tuple(pop + dpos))
            stack.append(tuple(pop + dneg))

    return False


ans = 0
for x, y, z in tqdm(filled):
    covered = 0

    pos = np.array((x, y, z))

    for coord in range(3):
        dpos = np.array([0, 0, 0])
        dpos[coord] = 1

        dneg = np.array([0, 0, 0])
        dneg[coord] = -1

        for nbr in [tuple(pos + dpos), tuple(pos + dneg)]:
            ans += exposed(nbr)


print(ans)
