with open("./day_06.in") as fin:
    data = fin.read().strip()

i = 0
while True:
    s = data[i:(i+4)]
    if len(set(list(s))) == 4:
        print(i + 4)
        break

    i += 1
