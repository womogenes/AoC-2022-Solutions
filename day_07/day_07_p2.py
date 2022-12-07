from collections import defaultdict
from functools import lru_cache

with open("./day_07.in") as fin:
    blocks = ("\n" + fin.read().strip()).split("\n$ ")[1:]


path = []

dir_sizes = defaultdict(int)
children = defaultdict(list)
visited = set()


def parse(block):
    lines = block.split("\n")
    command = lines[0]
    outputs = lines[1:]

    parts = command.split(" ")
    op = parts[0]
    if op == "cd":
        if parts[1] == "..":
            path.pop()
        else:
            path.append(parts[1])

        return

    abspath = "/".join(path)

    assert op == "ls"

    sizes = []
    for line in outputs:
        if not line.startswith("dir"):
            sizes.append(int(line.split(" ")[0]))
        else:
            dir_name = line.split(" ")[1]
            children[abspath].append(f"{abspath}/{dir_name}")

    dir_sizes[abspath] = sum(sizes)


for block in blocks:
    parse(block)


# Do DFS
@lru_cache(None)
def dfs(abspath):
    size = dir_sizes[abspath]
    for child in children[abspath]:
        size += dfs(child)
    return size


unused = 70000000 - dfs("/")
required = 30000000 - unused

ans = 1 << 60
for abspath in dir_sizes:
    size = dfs(abspath)
    if size >= required:
        ans = min(ans, size)

print(ans)
