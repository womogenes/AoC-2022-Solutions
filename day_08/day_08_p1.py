import numpy as np

with open("./day_08.in", "r") as fin:
    lines = fin.read().strip().split()

print(lines)
grid = [list(map(int, list(line))) for line in lines]

n = len(grid)
m = len(grid[0])

grid = np.array(grid)

ans = 0
for i in range(n):
    for j in range(m):
        h = grid[i, j]

        if j == 0 or np.amax(grid[i, :j]) < h:
            ans += 1
        elif j == m - 1 or np.amax(grid[i, (j+1):]) < h:
            ans += 1
        elif i == 0 or np.amax(grid[:i, j]) < h:
            ans += 1
        elif i == n - 1 or np.amax(grid[(i+1):, j]) < h:
            ans += 1

print(ans)
