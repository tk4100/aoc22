elf_cals = []
this = 0
with open("input.txt", "r") as fh:
    for line in fh:
        if line == "\n":
            elf_cals.append(this)
            this = 0
            continue

        this += int(line)

i = 3
ultramax = 0
while i > 0:
    thismax = max(elf_cals)
    ultramax += thismax
    del(elf_cals[elf_cals.index(thismax)])
    i -= 1
print("Most = {}, ULTRAMAX = {}".format(max(elf_cals), ultramax))
