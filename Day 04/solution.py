with open('input.txt') as f:
    lines = f.readlines()
  
# Set empty counters
total_overlap = 0
any_overlap = 0
  
  
# Iterate over input, strip out integers as strings and assign to vars  
for line in lines:
    elf1, elf2 = line.strip().split(',')
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')
   
    # Convert strings to ints for comparison
    elf1_start = int(elf1_start)
    elf1_end = int(elf1_end)
    elf2_start = int(elf2_start)
    elf2_end = int(elf2_end)
    
    # Increment counter upon find. First comparison is beginning, second is end
    # Check for complete overlap
    if elf1_start <= elf2_start and elf1_end >= elf2_end:
        total_overlap += 1
    elif elf1_start >= elf2_start and elf1_end <= elf2_end:
        total_overlap += 1
    
    # Check for partial overlap
    if elf1_start <= elf2_end and elf1_start >= elf2_start:
        any_overlap += 1
    elif elf2_start <= elf1_end and elf2_end >= elf1_start:
        any_overlap += 1


print("There are " + str(total_overlap) + " total overlapping sets")
print("There are " + str(any_overlap) + " overlapping sets")