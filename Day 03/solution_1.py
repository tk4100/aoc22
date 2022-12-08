with open('input.txt') as f:
    lines = f.readlines()
    
items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = 0

for line in lines:
    first, second = line.strip()[:len(line)//2], line[len(line)//2:]
    for char in first:
        if char in second:
            temp = 0
            temp += items.index(char) +
            score += temp
            print(temp)
            break
print(score)