#Author: Apostolos Chalis 2025
how_many_zeroes = 0
DIAL = 50

debug = False

with open("test", "r") as f:
    for raw in f:
        line = raw.strip()
        if not line:
            continue

        dir_char = line[0].upper()
        num_part = line[1:].strip()

        try:
            step = int(num_part)
        except ValueError:
            print("Skipping bad line:", repr(raw))
            continue

        if dir_char == "L":
            DIAL = (DIAL - step) % 100
        elif dir_char == "R":
            DIAL = (DIAL + step) % 100
        else:
            print("Skipping unknown direction:", line)
            continue

        if debug:
            print(f"{line} -> {DIAL}")

        if DIAL == 0:
            how_many_zeroes += 1

print(how_many_zeroes)

