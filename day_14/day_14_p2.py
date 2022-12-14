with open("./day_14.in") as fin:
    lines = fin.read().strip().split("\n")

sand_source = 500, 0

filled = set()
for line in lines:
    coords = []

    for str_coord in line.split(" -> "):
        x, y = map(int, str_coord.split(","))
        coords.append((x, y))

    for i in range(1, len(coords)):
        cx, cy = coords[i]  # cur
        px, py = coords[i - 1]

        if cy != py:
            assert cx == px
            for y in range(min(cy, py), max(cy, py) + 1):
                filled.add((cx, y))

        if cx != px:
            assert cy == py
            for x in range(min(cx, px), max(cx, px) + 1):
                filled.add((x, cy))


max_y = max([coord[1] for coord in filled])

# Fill with sand


def simulate_sand():
    global filled
    x, y = 500, 0

    if (x, y) in filled:
        return (x, y)

    while y <= max_y:
        if (x, y + 1) not in filled:
            y += 1
            continue

        if (x - 1, y + 1) not in filled:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in filled:
            x += 1
            y += 1
            continue

        # Everything filled, come to rest
        break

    return (x, y)


ans = 0

while True:
    x, y = simulate_sand()
    filled.add((x, y))
    ans += 1

    if (x, y) == (500, 0):
        break

print(ans)
