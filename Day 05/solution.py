with open('input.txt') as f:
    lines = f.readlines()

starting_state = [ [] for i in range(int(len(lines[0]) // 4)) ]
    
### Parse initial game state, break loop at end of gameboard

for line in lines:
    # Read lines until newline, break loop on newline
    if line != "\n":
        # First relevant char is at index 1, increment index by 4 as every 4th char is interesting
        index = 1
        # Determine how long to run loop. Take char count of first line, divide by 4 to find number of stacks
        for i in range(int(len(line)) // 4):
            if line[index] != " ":
                # break on name of stack to prevent it from joining stack
                if line[index].isnumeric() == False:
                    # Insert at beginning of list to prevent having to reverse lists later
                    starting_state[i].insert(0, line[index])
                else:
                    break
            index += 4           
    else:
        break

### Iterate over file ignoring gameboard looking for move instructions.
for line in lines:
    # Check if line is instruction
    if line[0] == "m":
        # split line into list of strings
        move = line.strip().split(' ')
        
        # define interesting strings as variables
        number_of_crates = int(move[1])
        source = int(move[3])
        destination = int(move[5])
        # slice up sublists, define package var as list of crates to move
        package = starting_state[source - 1][-number_of_crates:]
        starting_state[destination - 1].extend(package[::-1])
        del starting_state[source - 1][-number_of_crates:]

answer = ""

### Iterate over final state and pull top crate
for element in starting_state:
    answer += element[-1]
    
print(answer)

