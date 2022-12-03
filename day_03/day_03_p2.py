from string import ascii_lowercase, ascii_uppercase

key = ascii_lowercase + ascii_uppercase

with open("./day_03.in") as fin:
    data = fin.read().strip()


ans = 0

lines = data.split("\n")
for i in range(0, len(lines), 3):
    a = lines[i:(i + 3)] # The group of three Elves' rucksacks

    for i, c in enumerate(key):
        if all([c in li for li in a]):
            ans += key.index(c) + 1

print(ans)
