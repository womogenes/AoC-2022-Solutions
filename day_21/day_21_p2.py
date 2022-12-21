from functools import lru_cache
from sympy import symbols, solve_linear
from sympy.parsing.sympy_parser import parse_expr

with open("./day_21.in") as fin:
    lines = fin.read().strip().split("\n")


lookup = {}

humn = symbols("humn")


@lru_cache(None)
def compute(name):
    if name == "humn":
        return humn

    if isinstance(lookup[name], int):
        return lookup[name]

    parts = lookup[name]

    left = compute(parts[0])
    right = compute(parts[2])

    return parse_expr(f"({left}){parts[1]}({right})")


for line in lines:
    parts = line.split(" ")

    monkey = parts[0][:-1]

    if len(parts) == 2:
        lookup[monkey] = int(parts[1])
    else:
        lookup[monkey] = parts[1:]


left = compute(lookup["root"][0])
right = compute(lookup["root"][2])

ans = solve_linear(left, right)[1]
print(ans)
