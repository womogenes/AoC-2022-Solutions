from math import lcm
from heapq import heappop, heappush
from icecream import ic

with open("./day_24.in") as fin:
    lines = fin.read().strip().split("\n")


n = len(lines)
m = len(lines[0])

start = (0, 1)
end = (n - 1, m - 2)

# Things wrap after lcm(n, m) steps
period = lcm(n - 2, m - 2)

# Calculate blizzard positions after every point
arrows = ">v<^"

dirs = dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

storms = set()
for i in range(n):
    for j in range(m):
        c = lines[i][j]
        if c in arrows:
            storms.add((i, j, arrows.index(c)))


states = [None] * period
states[0] = storms
for t in range(1, period):
    new_storms = set()

    for storm in storms:
        row, col, d = storm
        drow, dcol = dirs[d]
        new_row, new_col = row + drow, col + dcol

        if new_row == 0:
            assert d == 3
            new_row = n - 2
        elif new_row == n - 1:
            assert d == 1
            new_row = 1

        if new_col == 0:
            assert d == 2
            new_col = m - 2
        elif new_col == m - 1:
            assert d == 0
            new_col = 1

        new_storms.add((new_row, new_col, d))

    states[t] = new_storms
    storms = new_storms  # Update


def grid_state(storms):
    ans = [["."] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i in [0, n - 1] or j in [0, m - 1]) and not (i, j) in [start, end]:
                ans[i][j] = "#"
                continue

            for d in range(4):
                if (i, j, d) in storms:
                    if isinstance(ans[i][j], int):
                        ans[i][j] += 1
                    elif ans[i][j] != ".":
                        ans[i][j] = 2
                    else:
                        ans[i][j] = arrows[d]

    return ans


def print_grid(grid):
    print("\n".join(["".join(map(str, row)) for row in grid]))


def occupied(loc, st):
    for d in range(4):
        if (loc[0], loc[1], d) in st:
            return True
    return False


# Go go go
pq = [(0, start, False, False)]
visited = set()

while len(pq) > 0:
    top = heappop(pq)
    if top in visited:
        continue
    visited.add(top)

    t, loc, hit_end, hit_start = top
    row, col = loc

    assert not (hit_start and not hit_end)

    assert not occupied(loc, states[t % period])

    if loc == end:
        if hit_end and hit_start:
            print(t)
            break

        hit_end = True

    if loc == start:
        if hit_end:
            hit_start = True

    # Go through neighbors
    for drow, dcol in (dirs + [[0, 0]]):
        new_row, new_col = row + drow, col + dcol
        new_loc = (new_row, new_col)

        # Within bounds?
        if (not new_loc in [start, end]) \
            and not (1 <= new_row <= n - 2
                     and 1 <= new_col <= m - 2):
            continue

        # Check if hitting a blizzard
        if occupied(new_loc, states[(t + 1) % period]):
            continue

        new_state = (t + 1, new_loc, hit_end, hit_start)
        heappush(pq, new_state)
