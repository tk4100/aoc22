tree = {}
tree["A"] = { "X": 3 + 1, "Y": 6 + 2, "Z": 0 + 3 }
tree["B"] = { "X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3 }
tree["C"] = { "X": 6 + 1, "Y": 0 + 2, "Z": 3 + 3 }

points = 0

with open("input.txt") as fh:
    for line in fh:
        elf, me = line.strip().split()

        points += tree[elf][me]

print("Total points: {}".format(points))
