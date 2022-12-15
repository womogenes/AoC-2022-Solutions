from tqdm import tqdm

with open("./day_15.in") as fin:
    lines = fin.read().strip().split("\n")


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


sensors = []
beacons = []
for line in lines:
    parts = line.split(" ")

    sx = int(parts[2][2:-1])
    sy = int(parts[3][2:-1])
    bx = int(parts[8][2:-1])
    by = int(parts[9][2:])

    sensors.append((sx, sy))
    beacons.append((bx, by))


N = len(sensors)
dists = []

for i in range(N):
    dists.append(dist(sensors[i], beacons[i]))

Y = 2000000

intervals = []

for i, s in enumerate(sensors):
    dx = dists[i] - abs(s[1] - Y)

    if dx <= 0:
        continue

    intervals.append((s[0] - dx, s[0] + dx))


# INTERVAL OVERLAP ETC.
allowed_x = []
for bx, by in beacons:
    if by == Y:
        allowed_x.append(bx)

print(allowed_x)

min_x = min([i[0] for i in intervals])
max_x = max([i[1] for i in intervals])

ans = 0
for x in range(min_x, max_x + 1):
    if x in allowed_x:
        continue

    for left, right in intervals:
        if left <= x <= right:
            ans += 1
            break


print(ans)
