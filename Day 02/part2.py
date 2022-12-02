tree = {}
tree["A"] = { "X": 0 + 3, "Y": 3 + 1, "Z": 6 + 2 }
tree["B"] = { "X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3 }
tree["C"] = { "X": 0 + 2, "Y": 3 + 3, "Z": 6 + 1 }

points = 0

with open("input.txt") as fh:
    for line in fh:
        elf, me = line.strip().split()

        points += tree[elf][me]

print("Total points: {}".format(points))
