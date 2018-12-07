from collections import Counter

print("Advent Of Code - Day 2")

PUZZLEINPUT = open('input.txt', 'r').read()
twos = 0
threes = 0


for line in PUZZLEINPUT.split():
    b = Counter(line)
    if b.most_common(3)[0][1]==3 or b.most_common(3)[1][1]==3:
        threes +=1
    if b.most_common(3)[0][1]==2 or b.most_common(3)[1][1]==2 or b.most_common(3)[2][1]==2:
        twos +=1

print("Part 1: Checksum: {}".format(threes*twos))

boxIds = PUZZLEINPUT.split()
boxIds = (sorted(boxIds))


for boxOne in boxIds:
    for boxTwo in boxIds:
            
            print(boxOne)
            print(boxTwo)
            break
