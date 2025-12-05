# Author: Apostolos Chalis 2025
import math 

invalid_ids = []

def solution(cont): 
    for item in cont.split(","): 
        rang = item.replace("\n", "")
        
        p1, p2 = rang.split("-")
        p1, p2 = int(p1), int(p2)
        for i in range(p1, p2+1): 
            length = int(math.log10(abs(i))) + 1

            if length%2 != 0: 
                print("Odd detected, breaking loop")
                continue

            mid = length // 2 
            divisor = 10 ** (length - mid)

            first_half = i // divisor
            fh = str(first_half)
            second_half = i % divisor 
            sh = str(second_half)
            
            if fh == sh:
                print("This index has been flagged: ", i)
                invalid_ids.append(i)

            num_to_work = str(i)
            if num_to_work[0] == "0": 
                invalid_ids.append(num_to_work)

with open("data", "r") as file: 
    content = file.read()

solution(content)
print(sum(invalid_ids))
