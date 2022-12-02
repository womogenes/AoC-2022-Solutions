with open("./day_02.in") as fin:
    lines = fin.read().strip().split("\n")


play_map = {"A": 0, "B": 1, "C": 2,
            "X": 0, "Y": 1, "Z": 2}

score_key = [1, 2, 3]

score = 0
for line in lines:
    opp, me = [play_map[i] for i in line.split()]

    # Win
    if (me - opp) % 3 == 1:
        score += 6
    elif (me == opp):
        score += 3

    score += score_key[me]


print(score)
