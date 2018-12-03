print("Advent Of Code - Day 1")


PUZZLEINPUT = open('input.txt', 'r').read()

changes = sum(int(n) for n in PUZZLEINPUT.split())
print("Part 1: Frequency Changes: {}".format(changes))