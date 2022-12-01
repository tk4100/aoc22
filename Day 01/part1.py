# list of all sums
elf_cals = []

# the current sum
this = 0
with open("input.txt", "r") as fh:
    for line in fh:
    
        # if we see an empty line, append our current total
        # to the list of sums, clear the counter, and 
        # proceed to the next input line
        if line == "\n":
            elf_cals.append(this)
            this = 0
            continue

        # cast this line's data into an int, and accumulate
        # it into the current running sum.
        this += int(line)

# use the max() python language feature to find the highest
# value in our array of sums
print("Most = {}".format(max(elf_cals)))
