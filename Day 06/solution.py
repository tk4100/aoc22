with open('input.txt') as f:
    text = f.read()
  
for i in range(len(text)):
    header = set(text[i:i+4])
    if len(header) == 4:
        print(i + 4)
        break
    
