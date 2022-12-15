from tqdm import tqdm

with open("./day_15.in") as fin:
    lines = fin.read().strip().split("\n")


# def dist(x1, y1, x2, y2):
#     return abs(x1 - x2) + abs(y1 - y2)

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


pos_lines = []
neg_lines = []

for i, s in enumerate(sensors):
    d = dists[i]
    neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
    pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])


pos = None
neg = None

for i in range(2 * N):
    for j in range(i + 1, 2 * N):
        a, b = pos_lines[i], pos_lines[j]

        if abs(a - b) == 2:
            pos = min(a, b) + 1

        a, b = neg_lines[i], neg_lines[j]

        if abs(a - b) == 2:
            neg = min(a, b) + 1


x, y = (pos + neg) // 2, (neg - pos) // 2
ans = x * 4000000 + y
print(ans)
