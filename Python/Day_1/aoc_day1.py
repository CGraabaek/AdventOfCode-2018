import itertools as iter
print("Advent Of Code - Day 1")

PUZZLEINPUT = open('input.txt', 'r').read()

data = [int(n) for n in PUZZLEINPUT.split()]
changes = sum(data)
print("Part 1: Frequency Changes: {}".format(changes))

total_freq = 0 
seen_set = {0}

for n in iter.cycle(data):
    total_freq += n
    if total_freq in seen_set:
        print("Part 2: First duplicate: {}".format(total_freq))
        break
    else:
        seen_set.add(total_freq)
        
