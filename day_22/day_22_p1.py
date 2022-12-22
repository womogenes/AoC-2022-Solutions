from collections import defaultdict
from pprint import pprint

with open("./day_22.in") as fin:
    # Assumes input ends with newline character
    parts = fin.read()[:-1].split("\n\n")

board = parts[0].split("\n")
path = parts[1]

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

visited = {}

for cmd in commands:
    visited[(row, col)] = ">V<^"[direction]

    if isinstance(cmd, str):
        if cmd == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

        continue

    # Move!
    drow, dcol = dirs[direction]

    for _ in range(cmd):
        visited[(row, col)] = ">V<^"[direction]
        if (row, col) not in adj:
            break

        new_row = row + drow
        new_col = col + dcol

        if drow != 0:
            rbounds = bound_col[col]
            height = rbounds[1] - rbounds[0] + 1
            new_row = (new_row - rbounds[0]) % height + rbounds[0]

        if dcol != 0:
            cbounds = bound_row[row]
            width = cbounds[1] - cbounds[0] + 1
            new_col = (new_col - cbounds[0]) % width + cbounds[0]

        if (new_row, new_col) not in adj:
            break

        row, col = new_row, new_col


ans = 1000 * (row + 1) + 4 * (col + 1) + direction
print(ans)
