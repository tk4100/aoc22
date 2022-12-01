elf_cals = []
this = 0
with open("input.txt", "r") as fh:
    for line in fh:
        if line == "\n":
            elf_cals.append(this)
            this = 0
            continue

        this += int(line)

print("Most = {}".format(max(elf_cals)))
