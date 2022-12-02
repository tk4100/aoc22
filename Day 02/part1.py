plays = { "A": 0, "B": 1, "C": 2 }
challenges = { "X": 0, "Y": 1, "Z": 2 }

points = 0
with open("input.txt") as fh:
    for line in fh:
        play, challenge = line.strip().split()

        points += challenges[challenge] + 1

        print(challenges[challenge], plays[play])

        if challenges[challenge] == plays[play]:
            points += 3
        elif challenges[challenge] == plays[play] + 1 or challenges[challenge] == plays[play] - 2:
            points += 6
        elif challenges[challenge] == plays[play] - 1:
            points += 0

print("Total points: {}".format(points))
