instructions = []

with open("instructions.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            instructions.append(line)

position = 50
count = 0

for instr in instructions:
    direction = instr[0]
    steps = int(instr[1:])
    
    if direction == "R":
        position += steps
    else:
        position -= steps
    
    position = position % 100
    
    if position == 0:
        count += 1

print("Number of times dial pointed to 0:", count)