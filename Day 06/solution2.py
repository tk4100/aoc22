with open('input.txt') as f:
    text = f.read()
  
for i in range(len(text)):
    header = set(text[i:i+14])
    if len(header) == 14:
        print(i + 14)
        break