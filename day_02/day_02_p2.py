with open("./day_02.in") as fin:
    lines = fin.read().strip().split("\n")


# X, Y, Z values represent offset in what to play
play_map = {"A": 0, "B": 1, "C": 2,
            "X": -1, "Y": 0, "Z": 1}

score_key = [1, 2, 3]

score = 0
for line in lines:
    opp, result = [play_map[i] for i in line.split()]

    score += (result + 1) * 3
    score += score_key[(opp + result) % 3]


print(score)
