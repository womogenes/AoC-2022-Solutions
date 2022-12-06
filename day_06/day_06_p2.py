with open("./day_06.in") as fin:
    data = fin.read().strip()

i = 0
while True:
    s = data[i:(i+14)]
    if len(set(list(s))) == 14:
        print(i + 14)
        break

    i += 1
