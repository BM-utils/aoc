#Author: Ioannis Michadasis 2025
instructions = []

with open("instructions.txt", "r") as file:
    for line in file:
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

print(count)
