from functools import cmp_to_key

with open("./day_13.in") as fin:
    parts = fin.read().strip().replace("\n\n", "\n").split("\n")


def compare(a, b):
    if isinstance(a, list) and isinstance(b, int):
        b = [b]

    if isinstance(a, int) and isinstance(b, list):
        a = [a]

    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if a == b:
            return 0
        return -1

    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while i < len(a) and i < len(b):
            x = compare(a[i], b[i])
            if x == 1:
                return 1
            if x == -1:
                return -1

            i += 1

        if i == len(a):
            if len(a) == len(b):
                return 0
            return 1  # a ended first

        # If i didn't hit the end of a, it hit the end of b first
        #   This means that b is shorter, which is bad
        return -1


lists = list(map(eval, parts))
lists.append([[2]])
lists.append([[6]])
lists = sorted(lists, key=cmp_to_key(compare), reverse=True)


for i, li in enumerate(lists):
    if li == [[2]]:
        a = i + 1
    if li == [[6]]:
        b = i + 1

print(a * b)
