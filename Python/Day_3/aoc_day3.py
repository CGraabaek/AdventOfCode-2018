import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import vizualisation

import re
print("Advent Of Code - Day 3")

PUZZLEINPUT = open('input.txt', 'r').readlines()

#Hold all claims
claims = []
# Match with raw strings
regex_pattern = r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

for line in PUZZLEINPUT:
    match = re.match(regex_pattern,line)
    claims.append([int(x) for x in match.groups()])


# Create 1000x1000 grid
N = 1000
squares = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        squares[i].append([])

# For all claims fill x-coordinates then y-coordinates with ID of box
for claim in claims: 
    for i in range(claim[1],claim[1]+claim[3]):
        for j in range(claim[2],claim[2]+claim[4]):
            squares[i][j].append(claim[0])

overlaps = 0

# Check for overlaps by checking for all arrays with 2 or more IDS
for k in range (N):
        for l in range (N):
                if len(squares[k][l]) >= 2:
                        overlaps += 1

print("Part 1: Overlaps: {}".format(overlaps))

def is_not_overlapping(claim):
        for i in range(claim[1],claim[1]+claim[3]):
                for j in range(claim[2],claim[2]+claim[4]):
                        if len(squares[i][j]) > 1:
                                return False
        return True           



for claim in claims:
        if(is_not_overlapping(claim)):
                break

print("Part 2: Not Overlapping: #{} X:{},Y:{}".format(claim[0],claim[1],claim[2]))

# See all the squares vizualized
vizualisation.plot_claims(claims,claim)
