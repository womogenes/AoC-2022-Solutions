with open("./day_22.in") as fin:
    # Assumes input ends with newline character
    parts = fin.read()[:-1].split("\n\n")

board = parts[0].split("\n")
path = parts[1]

debug = False

# Parse the path
idx = 0
commands = []
cur_num = ""
for idx in range(len(path)):
    if path[idx].isdigit():
        cur_num += path[idx]

    else:

        commands.append(int(cur_num))
        cur_num = ""
        commands.append(path[idx])

# If last command is a number
if cur_num != "":
    commands.append(int(cur_num))

# Possible orientations
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# Parse the board
nrows = len(board)
ncols = max([len(row) for row in board])

bound_row = [[ncols, -1] for _ in range(nrows)]
bound_col = [[nrows, -1] for _ in range(ncols)]

adj = set()
for row, line in enumerate(board):
    for col in range(len(line)):
        c = line[col]
        if c == ".":
            adj.add((row, col))

        if c in [".", "#"]:
            bound_row[row][0] = min(bound_row[row][0], col)
            bound_row[row][1] = max(bound_row[row][1], col)
            bound_col[col][0] = min(bound_col[col][0], row)
            bound_col[col][1] = max(bound_col[col][1], row)


# Do the instructions
direction = 0
row = 0
col = bound_row[0][0]

SCALE = 50  # Hard-coded

# MAP SOME EDGES TOGETHER
edge_map = [
    [[(0, 1), (0, 2), "^"], [(3, 0), (4, 0), "<"]],  # good
    [[(0, 2), (0, 3), "^"], [(4, 0), (4, 1), "v"]],  # good
    [[(0, 3), (1, 3), ">"], [(3, 2), (2, 2), ">"]],  # good
    [[(1, 2), (1, 3), "v"], [(1, 2), (2, 2), ">"]],  # good
    [[(3, 1), (3, 2), "v"], [(3, 1), (4, 1), ">"]],  # good
    [[(2, 0), (3, 0), "<"], [(1, 1), (0, 1), "<"]],  # good
    [[(2, 0), (2, 1), "^"], [(1, 1), (2, 1), "<"]]   # good
]


def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1


def add(a, b):
    """Because I don't want to have to use numpy"""
    a_copy = list(a)
    for i in range(len(a)):
        a_copy[i] += b[i]
    return tuple(a_copy)


def mult(a, k):
    """Also because I don't want to have to use numpy"""
    a_copy = list(a)
    for i in range(len(a)):
        a_copy[i] *= k
    return tuple(a_copy)


for i in range(len(edge_map)):
    for j in range(2):
        edge_map[i][j][2] = ">v<^".index(edge_map[i][j][2])
        for k in range(2):
            edge_map[i][j][k] = mult(edge_map[i][j][k], SCALE)


def along_edge_dir(edge):
    """
    Return the vector along the edge
    For instance, (8, 12) -> (8, 8) produces (0, -1)
    """
    start, end, _ = edge
    return sign(end[0] - start[0]), sign(end[1] - start[1])


# Off-by-one errors if edge is backwards
for i in range(len(edge_map)):
    for j in range(2):
        edge = edge_map[i][j]
        along = along_edge_dir(edge)

        if along[0] < 0 or along[1] < 0:
            edge[0] = add(edge[0], along)
            edge[1] = add(edge[1], along)

        edge_map[i][j] = edge


def off_edge(point, edge, direction):
    """
    Did we just walk off this edge?
    If so, returns the index along this edge
    """
    start, end, edge_dir = edge

    if edge_dir != direction:
        return None

    # Up- and left- facing edges need to modify a bit
    if direction in [2, 3]:
        start = add(start, dirs[direction])
        end = add(end, dirs[direction])

    # Walk from start vertex to end vertex, can't be that bad right?
    idx = 0

    drow, dcol = along_edge_dir(edge)  # NOT dirs[direction]
    row, col = start[0], start[1]

    for idx in range(SCALE):
        # This is all about wrapping at this point
        if (row, col) == point:
            return idx

        row += drow
        col += dcol

    return None


def point_at(edge, idx):
    assert idx < SCALE

    start, end, edge_dir = edge
    drow, dcol = along_edge_dir(edge)

    # FLIP THE OTHER WAY
    if edge_dir in [0, 1]:
        start = add(start, mult(dirs[edge_dir], -1))
        end = add(end, mult(dirs[edge_dir], -1))

    return add(start, mult((drow, dcol), idx))


def wrap(row, col, direction):
    """
    Return new point and new direction
    """
    idx = None

    for e1, e2 in edge_map:
        # Did we just walk off this edge?
        idx = off_edge((row, col), e1, direction)
        if isinstance(idx, int):
            debug and (f"match with {(row, col), e1, direction}")
            break

        idx = off_edge((row, col), e2, direction)
        if isinstance(idx, int):
            debug and (idx)
            debug and (f"match with {(row, col), e2, direction}")
            e1, e2 = e2, e1  # Swap them around
            break

    if idx == None:
        return (row, col, direction)

    debug and (e2, idx)

    assert idx == off_edge((row, col), e1, direction)

    # We go from e1 to e2
    new_point = point_at(e2, idx)

    # e2[2] is the direction of the edge pointing OUT
    new_direction = [2, 3, 0, 1][e2[2]]
    # This remaps it to point inwards

    return new_point[0], new_point[1], new_direction


""" row, col = 3, 6
debug and (wrap(row, col, 3))

exit() """


for cmd in commands:
    debug and (f"\n=== parsing [{cmd}] ===")

    if isinstance(cmd, str):
        if cmd == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

        debug and (f"    switched direction to {dirs[direction]}")

        continue

    # Move!
    for _ in range(cmd):
        drow, dcol = dirs[direction]

        debug and (f"    currently at {row}, {col}")
        debug and (
            f"    heading in direction {drow}, {dcol} [direction {direction}]")
        if (row, col) not in adj:
            break

        new_row, new_col = row + drow, col + dcol

        debug and (
            f"      attempting to move to {new_row}, {new_col}, dir={direction}")

        new_new_row, new_new_col, new_direction = wrap(
            new_row, new_col, direction)

        if (new_new_row, new_new_col) != (new_row, new_col):
            debug and (f"      [!] wrapped to {new_new_row}, {new_new_col}")

        if (new_new_row, new_new_col) not in adj:
            debug and (f"      [*] hit a barrier, stopping")
            break

        row, col = new_new_row, new_new_col
        direction = new_direction


ans = 1000 * (row + 1) + 4 * (col + 1) + direction
print(ans)
