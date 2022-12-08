with open('input.txt') as f:
    lines = f.readlines()
    
items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = 0

line_position = 0

while line_position < len(lines):
    for char in lines[line_position]:
        if char in lines[line_position + 1]:
            if char in lines[line_position + 2]:
                score += items.index(char) + 1
                line_position += 3
                break                    
print(score)

    
             